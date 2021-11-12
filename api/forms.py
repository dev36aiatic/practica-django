from django import forms
from django.db.models import fields
from django.contrib.auth.forms import ReadOnlyPasswordHashField
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


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'id_num', 'profile_picture', 'password']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user