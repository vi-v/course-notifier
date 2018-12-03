from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView


# Create your views here.
class BotView(APIView):
    def get(self, request):
        return HttpResponse('bot')

    def post(self, request):
        print(request.data)
        return HttpResponse(request.data)
