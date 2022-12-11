from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_book'].empty_label = 'No book'

    class Meta:
        model = Post
        fields = ['post_book', 'information', 'creator']
        widgets = {
            'information': forms.Textarea(attrs={'cols': 120, 'rows': 40})
        }

    def clean_information(self):
        information = self.cleaned_data['information']
        if len(information) == 1:
            raise ValidationError('Len != 1')

        return information


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
