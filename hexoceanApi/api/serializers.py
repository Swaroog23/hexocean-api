from rest_framework import serializers
from .models import Image, AppUser

class ImageSerializer(serializers.ModelSerializer):

    image_name = serializers.SerializerMethodField('get_image_name')
    source = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('source', 'user_id', 'image_name')

    def get_image_name(self, obj):
        return obj.source.url.split("/")[-1]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
