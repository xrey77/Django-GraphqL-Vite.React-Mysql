from graphene_django import DjangoObjectType
from accounts.models import User

class UserModelType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "mobile", 
            "username", "password", "userpicture", "is_blocked", 
            "is_activated", "mailtoken", "qrcodeurl"
        )
