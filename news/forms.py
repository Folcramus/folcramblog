from django import forms
from django.contrib.auth.models import User
from prompt_toolkit.validation import ValidationError
from contact.models import Contact
from .models import Comments


class CommentForm(forms.ModelForm):
    """Форма комментариев к статьям
    """
    class Meta:
        model = Comments
        fields = ('text',)

        widgets = {
            "text" : forms.Textarea(attrs={'class':"form-control", 'id':"exampleFormControlTextarea1", 'rows':"3"})
        }











