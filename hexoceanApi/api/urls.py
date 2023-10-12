from django.urls import path

from . import views

urlpatterns = [
    path("image/", views.ImageView.as_view(), name='image'),
    path("uploads/<str:link>", views.get_thumbnail, name='get-thumbnail'),
    path("uploads/premium/<str:link>", views.get_premium_thumbnail, name='get-premium-thumbnail'),
    path("uploads/enterprise/<str:link>", views.get_original_image, name='get-original-image')
]