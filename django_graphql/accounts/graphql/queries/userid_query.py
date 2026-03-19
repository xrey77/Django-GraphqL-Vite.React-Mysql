import graphene
from graphql_jwt.decorators import login_required
from accounts.models import User
from accounts.graphql.types.userType import UserModelType

class UserId(graphene.ObjectType):
    user = graphene.Field(UserModelType, id=graphene.Int(required=True))

    @login_required
    def resolve_user(self, info, id):
        try:
            return User.objects.get(pk=id)        
        except User.DoesNotExist:
            return None

# ======GET USER BY ID===========
# query GetUserId($id: Int!) {
#   getuserId {
#     user(id: $id) {
#       id
#       firstName
#       lastName
#       email
#       mobile
#       username
#       isActivated
#       isBlocked
#       userpicture
#       qrcodeurl    
#     }
#     }
#   }


# ==========VARIABLES ============
# {
#   "id": "1"
# }

# HEADERS   
# {
#   "Authorization": "Token 9829ccc2e887645f6d0a6c95a6f3d983edbb64a3"
# }
