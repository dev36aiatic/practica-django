from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', { 'valor' : 'Hola soy una variable'}) 

def uwu(request):
    return HttpResponse('JAJAJAJJAJA')
