from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import *
from .forms import *
from project_final.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView, DetailView ,CreateView
from contact.models import Contact
from contact.forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm

    success_url = '/'
    template_name = 'form.html'




    def form_valid(self, form):
        if form.is_valid():


            cd = form.cleaned_data['email']


            form.save()
            send_mail(
                'Вы подписались на рассылку',
                'Вечер в хату',
                'ponopaytov@Gmail.com',
                [cd],
                fail_silently=False

                )


        return super().form_valid(form)