import graphene
from graphql_jwt.decorators import login_required
from accounts.graphql.types.userType import UserModelType 
from accounts.models import User

class UpadatePasswordResponse(graphene.ObjectType):
    message = graphene.String()

class UpdatePasswordMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        new_password = graphene.String(required=True)        

    message = graphene.String()

    @login_required
    def mutate(self, info, id, new_password):
        try:
            user = User.objects.get(pk=id)

            user.set_password(new_password)
            user.save()

            return UpdatePasswordMutation(
                message="You changed your password successfully.")
        except User.DoesNotExist:
            raise Exception("User not found.")

class Mutation(graphene.ObjectType):
    update_password = UpdatePasswordMutation.Field()

# ============REQUEST=========
# mutation UpdatePassword(
#   $id: Int!,
#   $newPassword: String!) {
#   updatePassword(
#     newPassword: $newPassword) {
#       message
#     }  
# }

# =======VARIABLES===========
# {
#   "id": 1,
#   "newPassword": "1",
# }