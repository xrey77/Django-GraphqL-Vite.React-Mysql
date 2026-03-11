import graphene
from .types import UserModelType
from accounts.models import UserModel

class UserQuery(graphene.ObjectType):
    all_items = graphene.List(UserModelType)
    getuser_id = graphene.Field(UserModelType, id=graphene.ID(required=True))

    def resolve_all_items(root, info):
        user = info.context.user

        if not user or not user.is_authenticated:
            raise Exception("Authentication required")        
        # if not user.is_authenticated:
        #      raise Exception("Authentication required")
                     
        return UserModel.objects.all()

    def resolve_getuser_id(root, info, id):
        user = info.context.user
        
        if not user.is_authenticated:
             raise Exception("Authentication required")
             

        try:
            return UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return None

# ==========REQUEST============
# -----------GET ALL USERS-----
# query accounts {
#   allItems {
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
