from django.db import models

# Create your models here.


class Course(models.Model):
    crn = models.CharField(max_length=10)
    name = models.CharField(max_length=100, default="New course")
    spots = models.IntegerField(default=0)

    def __str__(self):
        return "{0} CRN: {1} ID: {2}".format(self.name, self.crn, self.pk)
