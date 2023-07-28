import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Create superuser"""
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', email='admin@admin.ru', password='admin')