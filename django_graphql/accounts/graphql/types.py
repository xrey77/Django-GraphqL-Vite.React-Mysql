from graphene_django import DjangoObjectType
from accounts.models import UserModel

class UserModelType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = (
            "id", "first_name", "last_name", "email", "mobile", 
            "username", "password", "userpicture", "is_blocked", 
            "is_activated", "mailtoken", "qrcodeurl"
        )
