from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404, render
from api.forms import AddBoard
from .models import Board, Ideas, User
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

class AddBoardView(CreateView):
    model = Board
    form_class = AddBoard
    template_name= 'form-board.html'
    success_url ='/accounts/boards/new/'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['owner'] =  self.request.user
        return initial
