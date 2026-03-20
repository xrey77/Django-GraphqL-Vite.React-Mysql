import graphene
from graphql_jwt.decorators import login_required
from accounts.graphql.types.userType import UserModelType
from accounts.models import User

class UsersQuery(graphene.ObjectType):
    all_items = graphene.List(UserModelType)

    @login_required
    def resolve_all_items(root, info):
        user = info.context.user                     
        return User.objects.all()


# ==========REQUEST============
# query accounts {
#   usersQuery {
#     allItems {
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
#   }
# }

# HEADERS
# {
#   "Authorization": "Token 9829ccc2e887645f6d0a6c95a6f3d983edbb64a3"
# }


