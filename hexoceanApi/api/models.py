import os

from django.db import models
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User


class UserTier(models.Model):
    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=300)
    thumbnail_size = models.IntegerField()
    can_fetch_original_img = models.BooleanField(default=False)
    can_generate_link = models.BooleanField(default=False)

def upload_path(instance, filename):
    return os.path.join("uploads", filename)

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=160, unique=True)
    tier = models.ForeignKey(UserTier, on_delete=models.SET_NULL, null=True)

class Image(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    source = models.ImageField(
        upload_to=upload_path, 
        validators=[validate_image_file_extension]
        )
