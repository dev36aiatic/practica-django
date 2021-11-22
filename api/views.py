from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from api.forms import AddBoard, AddContact, AddIdea, AddReply, RegistrationForm
from django.shortcuts import redirect
from api.serializers import BoardSerializer, CreateIdeasSerializer, IdeasSerializer, UserSerializer
from .models import Board, Contact, Ideas, ReplyMessage, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib import messages
from django.http import Http404
from rest_framework import generics, permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Board.objects.all()

        if self.request.GET.get('status') == 'public':
            queryset = queryset = Board.objects.filter(status='PU')
        elif self.request.GET.get('status') == 'private':
            queryset = queryset = Board.objects.filter(status='PR')
        else:
           queryset = Board.objects.all()
        return queryset


class IdeasList(generics.ListAPIView):
    serializer_class = IdeasSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Ideas.objects.all()

        if self.request.GET.get('status') == 'public':
            queryset = queryset = Ideas.objects.filter(status='PU')
        elif self.request.GET.get('status') == 'private':
            queryset = queryset = Ideas.objects.filter(status='PR')
        else:
           queryset = Ideas.objects.all()
        return queryset


class CreateIdeas(generics.CreateAPIView):
    serializer_class = CreateIdeasSerializer
    permission_classes = [permissions.AllowAny]


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
        db_board = Board.objects.get(pk=self.kwargs.get('pk'))

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
                form.add_error(
                    field="owner", error="Este tablero es privado y solo el dueño del mismo puede añadir notas.")
                return super().form_invalid(form)

    def get_success_url(self):
        #print(self.pk)
        return reverse('create_idea', kwargs={'pk': self.pk})


class DeleteIdeaView(DeleteView):
    # specify the model you want to use
    model = Ideas
    form_class = AddIdea
    template_name = 'form-delete-idea.html'
    success_url = reverse_lazy('boards_id')

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

    def delete(self, request, *args, **kwargs):
        db_idea = Ideas.objects.get(pk=self.kwargs.get('pk'))
        db_board = Board.objects.get(pk=self.kwargs.get('pk2'))

        if ((str(db_idea.owner) == str(self.request.user.email)) or (str(db_board.owner) == str(self.request.user.email))):
            return super(DeleteIdeaView, self).delete(
                request, *args, **kwargs)
        else:
            messages.error(
                self.request, f"Solo puedes borrar la idea si eres el creador de la misma o el dueño del tablero")
            return redirect(reverse('delete_idea', kwargs={'pk2': self.kwargs.get('pk2'), 'pk': self.kwargs.get('pk')}))

    def get_success_url(self):
        return reverse('boards_id', kwargs={'pk': self.kwargs.get('pk2')})


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
        db_idea = Ideas.objects.get(pk=self.kwargs.get('pk'))
        db_board = Board.objects.get(pk=self.kwargs.get('pk2'))

        if ((str(db_idea.owner) == str(self.request.user.email)) or (str(db_board.owner) == str(self.request.user.email))):
            messages.success(
                self.request, f"La idea ha sido editada exitosamente!")
            self.pk2 = self.kwargs.get('pk2')
            return super().form_valid(form)
        else:
            messages.error(
                self.request, f"Solo puedes editar la idea si eres el creador de la misma o el dueño del tablero")
            form.add_error(
                field="owner", error="Solo puedes editar la idea si eres el creador de la misma  o el dueño del tablero")
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


class ProfileView(TemplateView):

    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context


class AboutView(TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context


class ServicesView(TemplateView):

    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        return context


class AllContactsView(TemplateView):

    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context


class ContactView(CreateView):

    form_class = AddContact
    template_name = 'form-contact.html'
    success_url = '/accounts/contact/'

    def form_valid(self, form):
        messages.success(
            self.request, f"El mensaje se ha enviado exitosamente, pronto nos pondremos en contacto contigo!")
        return super().form_valid(form)


class AddReplyView(CreateView):

    model = ReplyMessage
    form_class = AddReply
    template_name = 'form-reply-to.html'
    success_url = reverse_lazy('reply_to_contact')
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replies'] = ReplyMessage.objects.filter(
            contact=self.kwargs.get('pk'))
        context['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return initial

    def form_valid(self, form):
        messages.success(
            self.request, f"Mensaje enviado!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reply_to_contact', kwargs={'pk': self.kwargs.get('pk')})


class DeleteContactView(DeleteView):
    model = Contact
    form_class = AddContact
    template_name = 'form-delete-contact.html'
    success_url = reverse_lazy('all_contacts')
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('all_contacts'))


class EditContactView(UpdateView):
    model = Contact
    form_class = AddContact
    template_name = 'form-edit-contact.html'
    success_url = reverse_lazy('edit_contact')
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('all_contacts'))

    def form_valid(self, form):
        messages.success(
            self.request, f"El mensaje ha sido editado exitosamente!")
        return super().form_valid(form)

    def get_success_url(self):
        #print(self.pk)
        return reverse('edit_contact', kwargs={'pk': self.kwargs.get('pk')})
