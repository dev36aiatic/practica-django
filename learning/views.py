from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from api.models import Board

""" def home(request):
    return render(request, 'home.html', {'valor': 'Hola soy una variable'})
 """
class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all();
        return context
