from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = settings.ADMIN_USERNAME
            email = settings.ADMIN_EMAIL
            password = settings.ADMIN_INITIAL_PASSWORD
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print('Creating account for %s (%s)' % (username, email))

        else:
            print('Admin accounts can only be initialized if no Accounts exist')
