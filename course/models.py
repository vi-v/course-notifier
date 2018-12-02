from django.db import models

# Create your models here.


class Course(models.Model):
    crn = models.CharField(max_length=10)
    name = models.CharField(max_length=100, default="New course")
    spots = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {2} ({1})".format(self.pk, self.crn, self.name)
