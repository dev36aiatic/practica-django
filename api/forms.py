from django import forms
from django.db.models import fields
from .models import Board, User


class AddBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'owner', 'status')

        widgets = {
            'owner': forms.HiddenInput(),
        }
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)