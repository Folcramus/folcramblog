from django.shortcuts import render, get_object_or_404, redirect
from .forms import Registration , Login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from news import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile
from django.http import HttpResponse


class Registration(CreateView):
    model = User
    form_class = Registration
    template_name = 'registration.html'
    success_url = reverse_lazy('name')


    def form_valid(self, form):
        form_valid = super().form_valid(form)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class Logout(LogoutView):
    next_page = reverse_lazy('name')


class Login(LoginView):
    model = Login
    template_name = 'login.html'
    success_url = reverse_lazy('name')
    def get_success_url(self):
        return self.success_url


def profile(request, id):
    profile = Profile.objects.get(id=id)

    return render(request, 'Profile.html', locals())






