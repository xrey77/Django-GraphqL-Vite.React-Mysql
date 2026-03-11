from django.urls import path
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from accounts.schema import schema
from rest_framework.request import Request as DRFRequest

class DRFGraphQLView(GraphQLView):
    def parse_body(self, request):
        data = getattr(request, 'data', None)
        if isinstance(data, dict):
            return data
        return super().parse_body(request)

    def get_context(self, request):
        return request

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFGraphQLView, cls).as_view(*args, **kwargs)
        view = csrf_exempt(view)
        view = api_view(['GET', 'POST'])(view)
        view = authentication_classes([TokenAuthentication])(view)
        view = permission_classes([AllowAny])(view)        
        return view

urlpatterns = [
    path("graphql/", DRFGraphQLView.as_view(
        schema=schema, 
        graphiql=True,
    )),
]



# from django.urls import path
# from graphene_django.views import GraphQLView
# from accounts.schema import schema 

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import authentication_classes, permission_classes, api_view
# from .views import DRFAuthenticatedGraphQLView

# urlpatterns = [
#     # path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),    
#     path("graphql/", csrf_exempt(DRFAuthenticatedGraphQLView.as_view(graphiql=True, schema=schema))),

# ]
