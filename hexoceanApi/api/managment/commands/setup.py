from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from api.models import UserTier, AppUser

class Command(BaseCommand):
    help = "Create admin and basic user tiers"

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            print("Setup - STARTING")
            admin = User.objects.create_user(
                username="Admin",
                password="Admin123",
                is_superuser=True,
                is_staff=True
                )
            admin_tier = UserTier.objects.create(
                name="Enterprise",
                thumbnail_size=400,
                can_fetch_original_img=True,
                can_generate_link=True
            )

            UserTier.objects.create(
                name="Basic",
                thumbnail_size=200,
                can_fetch_original_img=False,
                can_generate_link=False
            )
            UserTier.objects.create(
                name="Premium",
                thumbnail_size=400,
                can_fetch_original_img=True,
                can_generate_link=False
            )

            AppUser.objects.create(
                user=admin,
                username=admin.username,
                tier=admin_tier
            )
        print("Setup - DONE")
            
