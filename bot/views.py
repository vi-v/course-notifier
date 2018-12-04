from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from course.cli import Parser


# Create your views here.
class BotView(APIView):
    def get(self, request):
        return HttpResponse('bot')

    def post(self, request):
        if 'text' in request.data:
            parser = Parser()
            parser.parse_input(request.data['text'])
            return HttpResponse(status=200)
        else:
            return HttpResponse('No text in data')
