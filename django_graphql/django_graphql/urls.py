# main urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from accounts.schema import schema
from rest_framework.request import Request as DRFRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from graphene_file_upload.django import FileUploadGraphQLView

class DRFGraphQLView(GraphQLView):
    def parse_body(self, request):
        data = getattr(request, 'data', None)
        if isinstance(request, getattr(self, 'request_class', object)):        
            return request.data            
        return super().parse_body(request)

    def get_context(self, request):
        return request

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)        
        view = csrf_exempt(view)
        view = api_view(['GET', 'POST'])(view)
        view = authentication_classes([TokenAuthentication])(view)
        view = permission_classes([AllowAny])(view)        
        return view

class MultipartDRFGraphQLView(FileUploadGraphQLView, DRFGraphQLView):
    pass

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def authenticated_graphql_view(request):
    return GraphQLView.as_view(graphiql=True)(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('home.urls')), 
    path('', include('products.urls')),
    
    path("graphql/", MultipartDRFGraphQLView.as_view(
        schema=schema, 
        graphiql=True,
    )),
]