import graphene
from graphql_jwt.decorators import login_required
from accounts.graphql.types.userType import UserModelType 
from graphql import GraphQLError
from accounts.models import User
import pyotp

class VerifyTotpMutation(graphene.Mutation):
    class Arguments:
        id =  graphene.Int(required=True)
        otp = graphene.String(required=True)        

    username=graphene.String()
    message = graphene.String()

    @login_required
    def mutate(self, info, id, otp):   
        try:
            user = User.objects.get(pk=id)

            secret = user.secretkey
            totp = pyotp.TOTP(secret)                
            isValid = totp.verify(otp)        
            if isValid:
                return VerifyTotpMutation(
                    username=user.username,
                    message="OTP code has been validated successfully.")
            else:    
                raise GraphQLError("Invalid OTP code, please try another 6 digit OTP code.")
            
        except User.DoesNotExist:
            raise Exception("User not found.")

class Mutation(graphene.ObjectType):
    activate_mfa = VerifyTotpMutation.Field()

# ============REQUEST=========
# mutation VerifyTotp($id: Int!, $otp: String!) {
#   verifyTotp(id: $id, otp: $otp) {
#     username
#     message
#   }
# }

# =======VARIABLES===========
# {
#   "id": 1,
#   "otp": "234234"
# }