from django.core.management.base import BaseCommand
from django.utils import timezone
from course.models import Course
from bot.models import Bot


class Command(BaseCommand):
    help = 'Add course by CRN'

    def handle(self, *args, **kwargs):
        crn = input('Course CRN > ')
        crn = crn.strip()
        name = input('Course name > ')
        name = name.strip()

        course = Course.objects.create(crn=crn, name=name)

        bot = Bot.objects.first()
        message = 'Added course: {0} - {1}'.format(course.crn, course.name)
        bot.send_message(message)
