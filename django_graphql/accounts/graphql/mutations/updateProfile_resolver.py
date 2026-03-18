import graphene
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 

class UpadateProfileResponse(graphene.ObjectType):
    message = graphene.String()

class UpdateProfileMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)        
        last_name = graphene.String(required=True)
        mobile = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, first_name, last_name, mobile):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Authentication required")

        if not user.is_active:
            raise Exception("This account is inactive.")

        user.first_name = first_name
        user.last_name = last_name
        user.mobile = mobile            
        user.save()

        return UpdateProfileMutation(
            message="You have updated your profile successfully."
        )

class Mutation(graphene.ObjectType):
    update_profile = UpdateProfileMutation.Field()

# ============REQUEST=========
# mutation UpdateProfile(
#   $firstName: String!,
#   $lastName: String!,
#   $mobile: String!) {    
#     updateMutation(
#       firstName: $firstName,
#       lastName: $lastName,
#       mobile: $mobile      
#     ) {
#     message
#     }
#   }

# =======VARIABLES===========
# {
#   "firstName": "Reynaldo",
#   "lastName": "Marquez-Gragasin",
#   "mobile": "+633424234"
# }