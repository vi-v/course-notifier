from django.apps import AppConfig


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        print('bot ready')
