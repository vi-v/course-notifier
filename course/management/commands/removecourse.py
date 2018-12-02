from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from course.models import Course
from bot.models import Bot


class Command(BaseCommand):
    help = 'Remove course by ID'

    def handle(self, *args, **kwargs):
        key = input('Course ID > ')
        key = key.strip()

        try:
            course = Course.objects.get(pk=key)
        except ObjectDoesNotExist:
            self.stdout.write('Course does not exist\n')
            return

        crn = course.crn
        name = course.name
        course.delete()

        bot = Bot.objects.first()
        message = 'Removed course: {0} - {1}'.format(crn, name)
        bot.send_message(message)
