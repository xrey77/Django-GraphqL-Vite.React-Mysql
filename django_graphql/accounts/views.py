# from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.authentication import TokenAuthentication
# from accounts.schema import schema

# @csrf_exempt
# @api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([AllowAny]) # Allows Login/Register mutations to run
# def drf_graphql_view(request):
#     return GraphQLView.as_view(schema=schema, graphiql=True)(request)

# urlpatterns = [
#     path("graphql/", drf_graphql_view),
# ]
