import graphene
from accounts.graphql.types.userType import UserModelType

class UserIdQuery(graphene.ObjectType):

    user = graphene.Field(UserModelType)

def resolve_user(self, info):
    user = info.context.user

    if user.is_anonymous:
        raise Exception("Authentication required")

    if not user.is_active:
        raise Exception("This account is inactive.")

    return user

# HEADERS   
# {
#   "Authorization": "Token 9829ccc2e887645f6d0a6c95a6f3d983edbb64a3"
# }


# ======GET USER BY ID===========
# query GetUser($id: ID!) {
#   getuserId(id: $id) {
#     id
#     firstName
#     lastName
#     email
#     mobile
#     username
#     isActivated
#     isBlocked
#     userpicture
#     qrcodeurl
#   }
# }

# ==========VARIABLES ============
# {
#   "id": "1"
# }
