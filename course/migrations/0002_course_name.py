# Generated by Django 2.1.3 on 2018-12-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='New course', max_length=100),
        ),
    ]
