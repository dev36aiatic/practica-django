from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

""" def home(request):
    return render(request, 'home.html', {'valor': 'Hola soy una variable'})
 """
class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """ context['users'] = User.objects.get(id=3); """
        return context
