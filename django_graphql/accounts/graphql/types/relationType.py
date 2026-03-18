import graphene
from graphene_django import DjangoObjectType
from accounts.models import User
from role.models import Role

class RoleType(DjangoObjectType):
    class Meta:
        model = Role
        fields = ("id", "name", "users") # 'users' comes from related_name

class UserType(DjangoObjectType):
    class Meta:
        model = User
        # Exclude sensitive fields like password
        exclude = ("password", "is_superuser") 

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    
    def resolve_all_users(root, info):
        return User.objects.select_related("role").all()
