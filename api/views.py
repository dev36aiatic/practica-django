from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from api.forms import AddBoard, AddIdea, RegistrationForm
from django.shortcuts import redirect
from .models import Board, Ideas
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib import messages
from django.http import Http404


class AddBoardView(CreateView):
    
    model = Board
    form_class = AddBoard
    template_name = 'form-board.html'
    success_url = '/accounts/boards/new/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['owner'] = self.request.user
        return initial

    def form_valid(self, form):
        messages.success(
            self.request, f"El tablero ha sido creado exitosamente!")
        return super().form_valid(form)


class AddIdeaView(CreateView):

    model = Ideas
    form_class = AddIdea
    template_name = 'form-idea.html'
    success_url = reverse_lazy('boards_id')
    pk = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.user
        context['board'] = Board.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['owner'] = self.request.user
        initial['board'] = Board.objects.get(pk=self.kwargs.get('pk'))
        initial['status'] = Board.objects.get(pk=self.kwargs.get('pk')).status
        return initial

    def form_valid(self, form):
        db_board =  Board.objects.get(pk=self.kwargs.get('pk'))

        if db_board.status == 'PU':
            messages.success(
                self.request, f"La idea ha sido añadida al tablero exitosamente!")
            self.pk = self.kwargs.get('pk')
            return super().form_valid(form)
        else:
            if (str(db_board.owner) == str(self.request.user.email)):  
                messages.success(
                    self.request, f"La idea ha sido añadida al tablero privado exitosamente!")
                self.pk = self.kwargs.get('pk')
                return super().form_valid(form)
            else:
                messages.error(
                    self.request, f"Este tablero es privado y solo el dueño del mismo puede añadir notas.")
                form.add_error(field="owner", error="Este tablero es privado y solo el dueño del mismo puede añadir notas.")
                return super().form_invalid(form)

    def get_success_url(self):
         #print(self.pk)
         return reverse('create_idea', kwargs={'pk': self.pk})

class EditIdeaView(UpdateView):

    model = Ideas
    form_class = AddIdea
    template_name = 'form-edit-idea.html'
    success_url = reverse_lazy('update_idea')
    pk2 = None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.user
        context['board'] = Board.objects.get(pk=self.kwargs.get('pk2'))
        context['idea'] = Ideas.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('boards_id',  kwargs={'pk': self.kwargs.get('pk2')}))

    def form_valid(self, form):
        db_idea =  Ideas.objects.get(pk=self.kwargs.get('pk'))

        if (str(db_idea.owner) == str(self.request.user.email)):
            messages.success(
                self.request, f"La idea ha sido editada exitosamente!")
            self.pk2 = self.kwargs.get('pk2')
            return super().form_valid(form)
        else:
            messages.error(
                self.request, f"Solo puedes editar la nota si eres el creador de la misma")
            form.add_error(field="owner", error="Solo puedes editar la nota si eres el creador de la misma")
            return super().form_invalid(form)    

    def get_success_url(self):
         #print(self.pk)
         return reverse('update_idea', kwargs={'pk2': self.kwargs.get('pk2'), 'pk': self.kwargs.get('pk')})


class BoardsView(TemplateView):

    template_name = 'boards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        context['public_boards'] = Board.objects.filter(status='PU')
        context['private_boards'] = Board.objects.filter(status='PR')
        context['my_boards'] = Board.objects.filter(owner=self.request.user.id)
        return context


class BoardDetailView(DetailView):

    model = Board
    template_name = 'board-detail.html'
    context_object_name = "board"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('boards'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ideas'] = Ideas.objects.filter(board=self.kwargs.get('pk'))

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
