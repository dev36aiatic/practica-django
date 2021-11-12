from django.views.generic.base import TemplateView
from api.forms import AddBoard, RegistrationForm
from .models import Board, Ideas, User
from django.views.generic.edit import CreateView
from django.urls import reverse


class AddBoardView(CreateView):
    model = Board
    form_class = AddBoard
    template_name = 'form-board.html'
    success_url = '/accounts/boards/new/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['owner'] = self.request.user
        return initial

class BoardsView(TemplateView):
    
    template_name = 'boards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context
           


class RegistrationView(CreateView):
    template_name = '../templates/account/signup.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context
