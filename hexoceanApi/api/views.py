from django.shortcuts import render
from django.http import FileResponse, StreamingHttpResponse, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions
from rest_framework.exceptions import UnsupportedMediaType, PermissionDenied
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ImageSerializer, UserSerializer
from .models import AppUser, Image
from .utils import prepare_links, prepare_image
    

class ImageView(LoginRequiredMixin, generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageSerializer

    def get_queryset(self):
        try:
            user = AppUser.objects.get(id=self.request.user.id)
            user_images = Image.objects.filter(user=user)
            return user_images
        except ObjectDoesNotExist:
            raise Http404()

    def post(self, request):
        image = request.data.get("source")
        user_id = request.user.id

        if image:
            try:
                app_user = AppUser.objects.get(user__id=user_id)

                image_to_save = Image(source=image, user_id=app_user.id)
                image_to_save.full_clean()
                image_to_save.save()

                serializer = ImageSerializer(image_to_save)
                
                return Response(prepare_links(app_user, serializer, request))
            
            except ObjectDoesNotExist:
                raise Http404("User not found")
            except ValidationError:
                raise UnsupportedMediaType(image.content_type)

        raise Http404("No image attached") 
    
@login_required
@api_view(('GET',))
def get_thumbnail(request, link):
    image = prepare_image(link, 200)
    return HttpResponse(image, content_type="jpeg/png")

@login_required
@api_view(('GET',))
def get_premium_thumbnail(request, link):
    try:
        user = AppUser.objects.get(id=self.request.user.id)
        if user.tier.name in ["Premium", "Enterprise"]:
            image = prepare_image(link, 400)
            return HttpResponse(image, content_type="jpeg/png")
        raise PermissionDenied("User Tier is not Premium")
    except ObjectDoesNotExist:
        raise Http404("User not found")


@login_required
@api_view(('GET',))
def get_original_image(request, link):
    try:
        user = AppUser.objects.get(id=self.request.user.id)
        if user.tier.name =="Enterprise":
            image = prepare_image(link, None)
            return HttpResponse(image, content_type="jpeg/png")
        raise PermissionDenied("User Tier is not Enterprise")
    except ObjectDoesNotExist:
        raise Http404("User not found")

