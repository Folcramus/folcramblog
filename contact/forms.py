from django import forms
from django.contrib.auth.models import User
from prompt_toolkit.validation import ValidationError

from .models import  Contact




class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact

        fields = ('email',)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control form-control-auto", "placeholder": "Your Email...", "id":"InputEmail2", "type":"email", "name":"email"}),

        }

        labels = {
            "email": '',


        }

    def clean(self):

            # данные из формы выбираются с помощью суперфункции

            super(ContactForm, self).clean()

            # извлечь имя пользователя и текстовое поле из данных

            email = self.cleaned_data.get('email')



            # условия, которые должны быть выполнены для длины имени пользователя

            if Contact.objects.filter(email=email):
                self._errors['email'] = self.error_class([

                    'Этот email уже подписан на рассылку'])






            # вернуть любые ошибки, если найдены

            return self.cleaned_data


class EmailForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = ('email',)
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email...", "id": "Email", "type": "email"}),

        }

        labels = {
            "email": '',

        }

    def clean(self):
        # данные из формы выбираются с помощью суперфункции

        super(EmailForm, self).clean()

        # извлечь имя пользователя и текстовое поле из данных

        email = self.cleaned_data.get('email')

        # условия, которые должны быть выполнены для длины имени пользователя

        if Contact.objects.filter(email=email):
            self._errors['email'] = self.error_class([

                'Этот email уже подписан на рассылку'])

        # вернуть любые ошибки, если найдены

        return self.cleaned_data














