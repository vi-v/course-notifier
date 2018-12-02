from django.core.management.base import BaseCommand
from django.utils import timezone
from course.models import Course


class Command(BaseCommand):
    help = 'List all courses'

    def handle(self, *args, **kwargs):
        for c in Course.objects.all():
            print(c)
