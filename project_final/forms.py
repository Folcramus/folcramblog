from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import News
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Registration(UserCreationForm, forms.ModelForm):




    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widgets.attrs['class'] = 'form-control'


class Login(AuthenticationForm, forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')


