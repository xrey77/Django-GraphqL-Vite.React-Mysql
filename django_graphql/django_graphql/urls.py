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
from graphene_file_upload.django import FileUploadGraphQLView
from django.utils.decorators import method_decorator

class MultipartDRFGraphQLView(FileUploadGraphQLView, GraphQLView):
    def get_context(self, request):
        # Ensure the context has the user from DRF
        return request

    def parse_body(self, request):
        # 1. Try standard Graphene-File-Upload logic first
        if request.content_type and 'multipart/form-data' in request.content_type:
            return self.parse_multipart(request)
        # 2. Fallback to DRF data if available
        if hasattr(request, 'data'):
            return request.data
            
        return super().parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        # DRF decorators here
        view = super().as_view(*args, **kwargs)
        view = api_view(['GET', 'POST'])(view)
        view = authentication_classes([TokenAuthentication])(view)
        view = permission_classes([AllowAny])(view)
        return view

class AuthenticatedGraphQLView(GraphQLView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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