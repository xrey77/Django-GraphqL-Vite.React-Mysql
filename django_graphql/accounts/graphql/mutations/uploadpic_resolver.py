import graphene
import os
from pathlib import Path
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 
from django.contrib.auth import get_user_model
from graphene_file_upload.scalars import Upload

User = get_user_model()

class UploadPictureResponse(graphene.ObjectType):
    message = graphene.String()

class UploadPictureMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)        

    message = graphene.String()

    def mutate(self, info, file):
        user = info.context.user
        
        if not user.is_authenticated:
            raise Exception("Authentication required")

        # 1. Define the target directory
        # Ensure this matches your actual STATICFILES_DIRS or static root path
        upload_path = os.path.join('static', 'users')
        full_directory_path = os.path.join(settings.BASE_DIR, upload_path)

        # 2. Create directory if it doesn't exist
        if not os.path.exists(full_directory_path):
            os.makedirs(full_directory_path)

        # 3. Construct the filename
        extension = Path(file.name).suffix
        new_filename = f"00{user.id}{extension}"
        file_save_path = os.path.join(full_directory_path, new_filename)

        # 4. Write the file to the filesystem
        with open(file_save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # 5. Save only the filename (or relative path) to the DB
        user.userpicture = new_filename
        user.save()

        return UploadPictureResponse(message="You have changed your profile picture successfully.")


class Mutation(graphene.ObjectType):
    upload_picture = UploadPictureMutation.Field()

# ============REQUEST=========
# const UPLOAD_MUTATION = gql`
#   mutation UploadPicture($file: Upload!) {
#     uploadPicture(imgFile: $file) {
#       message
#       success
#     }
#   }
# `;
