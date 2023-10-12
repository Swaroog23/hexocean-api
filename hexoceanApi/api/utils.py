from rest_framework.reverse import reverse
from .models import Image

from PIL import Image as PILImage
from io import BytesIO


def prepare_links(user, image_serializer, request):
    data = {}

    if user.tier.name in ["Basic", "Premium", "Enterprise"]:
        data["get-thumbnail-url"] = prepare_basic_tier_thumbnail_link(
            image_serializer, request
            )

    if user.tier.name in ["Premium", "Enterprise"]:
        data["get-premium-thumbnail"] = prepare_premium_tier_thumbnail_link(
            image_serializer, request
            )

    if user.tier.name == "Enterprise":
        data["get-original-image"] = prepare_enterprise_tier_thumbnail_link(
            image_serializer, request
            )

    return data

def prepare_basic_tier_thumbnail_link(image_serializer, request):
    return reverse('get-thumbnail', 
                    args=[image_serializer.data.get("image_name")],
                    request=request
                    )

def prepare_premium_tier_thumbnail_link(image_serializer, request):
    return reverse('get-premium-thumbnail', 
                args=[image_serializer.data.get("image_name")],
                request=request
                )

def prepare_enterprise_tier_thumbnail_link(image_serializer, request):
    return reverse('get-original-image', 
                args=[image_serializer.data.get("image_name")],
                request=request
                )

def prepare_image(link, size):
    image = Image.objects.get(source=f"uploads/{link}")
    byte = BytesIO()
    with PILImage.open(image.source) as img:
        if size:
            img.thumbnail((size,size))
        img.save(byte, img.format)

    prepared_image = byte.getvalue()
    
    return prepared_image
