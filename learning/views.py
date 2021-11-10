from django.http.response import HttpResponse
from django.views import View
from django.shortcuts import render
from rest_framework import viewsets
from learning.serializers import UserSerializer
from .models import User


def home(request):
    return render(request, 'home.html', {'valor': 'Hola soy una variable'})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


""" class User(View):
    users = User.objects.all()
    output = ''

    for user in users:
        output += f"{user.first_name } {user.last_name} {user.id} <br>" 

    def get(self, request):
        return HttpResponse(self.output) """

