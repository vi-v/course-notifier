import requests
from django.db import models
from course.models import Course
# Create your models here.


class Bot(models.Model):
    bot_id = models.CharField(max_length=100)

    def notify(self, course):
        self.send_message(course.name + ' ' + str(course.spots) + ' available')

    def send_message(self, message):
        payload = {
            "bot_id": self.bot_id,
            "text": message
        }

        requests.post('https://api.groupme.com/v3/bots/post', data=payload)
