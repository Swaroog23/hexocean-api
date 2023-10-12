import pytest
import json

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.reverse import reverse

from .models import AppUser, UserTier

@pytest.fixture
@pytest.mark.django_db
def user_fixture(db):
    user = User.objects.create_user(username="TEST", password="test_password")
    user_tier = UserTier.objects.create(
        name="Enterprise",
        thumbnail_size=400,
        can_fetch_original_img=True,
        can_generate_link=True
    )
    
    return AppUser.objects.create(username="TEST", tier=user_tier, user=user)


def test_image_GET(user_fixture, db, client):
    client.login(username="TEST", password="test_password")
    response = client.get(reverse("image"))

    assert response.status_code == 200

def test_image_POST(user_fixture, db, client):
    client.login(username="TEST", password="test_password")

    image = SimpleUploadedFile("image.jpg", b"file_content", content_type="image/png")
    response_urls = ["get-thumbnail-url", "get-premium-thumbnail", "get-original-image"]

    response = client.post(reverse("image"), {"source": image})
    
    assert response.status_code == 200
    for url in response_urls:
        assert url in response.data
