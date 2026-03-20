import graphene
from graphql_jwt.decorators import login_required
from accounts.graphql.types.userType import UserModelType 
from accounts.models import User
import pyotp
import qrcode
import base64
from io import BytesIO
from PIL import Image

class ActivateMfaResponse(graphene.ObjectType):
    qrcodeurl = graphene.String()
    message = graphene.String()

class ActivateMfaMutation(graphene.Mutation):
    class Arguments:
        id =  graphene.Int(required=True)
        twofactorenabled = graphene.Boolean(required=True)        

    qrcodeurl=graphene.String()
    message = graphene.String()

    @login_required
    def mutate(self, info, id, twofactorenabled):
        user = User.objects.get(pk=id)
   
        if twofactorenabled:
            try:
                secret_key = pyotp.random_base32()    
                totp = pyotp.TOTP(secret_key)        
                qrcodeuri = totp.provisioning_uri(name=user.email, issuer_name='DIEBOLD-NIXDORF')
                qrcode_base64 = generate_qr_code_base64(qrcodeuri)                

                user.secretkey=secret_key
                user.qrcodeurl=qrcode_base64
                user.save()
                return ActivateMfaResponse(
                    qrcodeurl=qrcode_base64,
                    message="Multi-Factor Authenticator has been enabled successfully.")
            except User.DoesNotExist:
                raise Exception("User not found.")

        else:
            try:
                user.secretkey = None
                user.qrcodeurl=None
                user.save()
                return ActivateMfaResponse(
                    qrcodeurl=None,
                    message="Multi-Factor Authenticator has been disabled successfully.")
            except User.DoesNotExist:
                raise Exception("User not found.")

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
# mutation ActivateMfa($id: Int!, $twofactorenabled: Boolean!){
#   activateMfa(id: $id, twofactorenabled: $twofactorenabled) {
#     qrcodeurl
#     message
#   }
# }

# =======VARIABLES===========
# {
#   "id": 1,
#   "twofactorenabled": false
# }