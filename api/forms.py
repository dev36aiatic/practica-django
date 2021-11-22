from django import forms
from .models import Board, Contact, Ideas, ReplyMessage, User


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

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AddReply(forms.ModelForm):
    class Meta:
        model = ReplyMessage
        fields = ('reply', 'contact')
        
        widgets = {
            'contact': forms.HiddenInput(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddIdea(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('board', 'owner', 'name','status')

        widgets = {
            'owner': forms.HiddenInput(),
            'board': forms.HiddenInput(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name',
                  'last_name', 'id_num', 'profile_picture', 'password']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
