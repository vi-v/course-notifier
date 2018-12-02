"""course_notifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
from django.contrib import admin
from django.urls import path
from bot.models import Bot
from course import poll


urlpatterns = [
    path('admin/', admin.site.urls),
]

if 'runserver' in sys.argv:
    if len(Bot.objects.all()) == 0:
        bot_id = input('Enter bot id > ')
        Bot.objects.create(bot_id=bot_id)

    bot = Bot.objects.first()
    bot.send_message('Server started')
    poll.run()
