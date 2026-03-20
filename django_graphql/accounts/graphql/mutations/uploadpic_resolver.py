import graphene
import os
from graphql_jwt.decorators import login_required
from accounts.models import User
from pathlib import Path
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 
from graphene_file_upload.scalars import Upload

class UploadPictureResponse(graphene.ObjectType):
    userpicture = graphene.String()
    message = graphene.String()

class UploadPictureMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        file = Upload(required=True)

    userpicture = graphene.String()
    message = graphene.String()

    @login_required
    def mutate(self, info, id, file):
        try:
            user = User.objects.get(pk=id)
            
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'static/users'))
            
            extension = Path(file.name).suffix
            filename = f"00{id}{extension}"
            
            # if fs.exists(filename):
            #     fs.delete(filename)
                
            fs.save(filename, file)

            user.userpicture = filename
            user.save()

            return UploadPictureMutation    (
                userpicture=user.userpicture,
                message="Profile picture updated successfully."
            )

        except User.DoesNotExist:
            raise GraphQLError("User not found")
                    
class Mutation(graphene.ObjectType):
    upload_picture = UploadPictureMutation.Field()

# ============REQUEST=========
# mutation UploadPicture($id: Int!, $file: Upload!) {
#   uploadPicture(id: $id, file: $file) {
#   	userpicture
#     message  
#   }
# }