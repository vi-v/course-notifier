# Generated by Django 2.1.3 on 2018-12-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='spots',
            field=models.IntegerField(default=0),
        ),
    ]
