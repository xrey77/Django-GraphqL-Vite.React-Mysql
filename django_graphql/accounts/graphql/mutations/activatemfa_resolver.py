import graphene
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 
from django.contrib.auth import get_user_model
import pyotp
import qrcode
import base64
from io import BytesIO
from PIL import Image


User = get_user_model()

class ActivateMfaResponse(graphene.ObjectType):
    qrcodeurl = graphene.String()
    message = graphene.String()

class ActivateMfaMutation(graphene.Mutation):
    class Arguments:
        twofactorenabled = graphene.Boolean(required=True)        

    qrcodeurl=graphene.String()
    message = graphene.String()

    def mutate(self, info, twofactorenabled):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Authentication required")

        if not user.is_active:
            raise Exception("This account is inactive.")

        if twofactorenabled:

            secret_key = pyotp.random_base32()    
            totp = pyotp.TOTP(secret_key)        
            qrcodeuri = totp.provisioning_uri(name=user.email, issuer_name='SUPERCARS INC.')
            qrcode_base64 = generate_qr_code_base64(qrcodeuri)                

            user.secretkey=secret_key
            user.qrcodeurl=qrcode_base64
            user.save()
            return ActivateMfaResponse(
                qrcodeurl=qrcode_base64,
                message="Multi-Factor Authenticator has been enabled successfully.")

        else:
            user.secretkey = None
            user.qrcodeurl=None
            user.save()
            return ActivateMfaResponse(
                qrcodeurl=None,
                message="Multi-Factor Authenticator has been disabled successfully.")

def generate_qr_code_base64(data):
    qr_img = qrcode.make(data)

    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    buffer.seek(0)
    
    encoded_img = base64.b64encode(buffer.read()).decode()
    
    qr_code_data = f'data:image/png;base64,{encoded_img}'
    
    return qr_code_data

class Mutation(graphene.ObjectType):
    activate_mfa = ActivateMfaMutation.Field()

# ============REQUEST=========
# mutation ActivateMfa($twofactorenabled: Boolean!){
#   activateMfa(twofactorenabled: $twofactorenabled) {
#     qrcodeurl
#     message
#   }
# }

# =======VARIABLES===========
# {
#   "twofactorenabled": false
# }