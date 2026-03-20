import graphene
from graphene_django import DjangoObjectType
from products.models import Product
from categories.models import Categories

class CategoryType(DjangoObjectType):
    class Meta:
        model = Categories
        fields = ("id", "name") 

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"
