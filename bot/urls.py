from django.urls import path
from bot.views import BotView

urlpatterns = [
    path('', BotView.as_view()),
]

