from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *arg, **options):
        superuser = User.objects.filter(email="admin@admin.com", username="admin", is_superuser=True)
        if superuser.exists():
            self.stdout.write("This admin is already in database!")
        else:
            User.objects.create_superuser(email="admin@admin.com", username="admin", password="Temp1234")
            self.stdout.write("Admin was created successfully!")
