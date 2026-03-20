import graphene
from graphql_jwt.decorators import login_required
from accounts.models import User
from accounts.graphql.types.userType import UserModelType 

class UpadateProfileResponse(graphene.ObjectType):
    message = graphene.String()

class UpdateProfileMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String(required=True)        
        last_name = graphene.String(required=True)
        mobile = graphene.String(required=True)

    message = graphene.String()

    @login_required
    def mutate(self, info, id, first_name, last_name, mobile):
        try:

            user = User.objects.get(pk=id)
            
            user.first_name = first_name
            user.last_name = last_name
            user.mobile = mobile            
            user.save()

            return UpadateProfileResponse(
                message="You have updated your profile successfully."
            )
        except User.DoesNotExist:
            raise Exception("User not found.")

class Mutation(graphene.ObjectType):
    update_profile = UpdateProfileMutation.Field()

# ============REQUEST=========
# mutation UpdateProfile(
#   id: Int!,
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
#   "id": 1,
#   "firstName": "Reynaldo",
#   "lastName": "Marquez-Gragasin",
#   "mobile": "+633424234"
# }