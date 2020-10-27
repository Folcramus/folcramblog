from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail , send_mail
from contact.models import Contact
from django.template.loader import render_to_string
from django.utils import timezone

class News(models.Model):

    name = models.CharField(max_length=260, default=None, blank=True)
    author = models.CharField(default=None, blank=True, max_length=64)

    text = RichTextUploadingField(blank=True, default=None, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "%s, %s" % (self.name , self.text)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'



class Comments(models.Model):
    """Ксласс комментариев к новостям
    """
    user = models.ForeignKey( User,verbose_name="Пользователь", on_delete=models.CASCADE)
    new = models.ForeignKey( News, verbose_name="Новость", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", default=timezone.now)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "%s" %(self.user)


@receiver(post_save, sender=News)
def create_user_profile(sender, instance, created,  *args, **kwargs):
    if created:
        def rass(id, name):



            news = News.objects.get(id=id, name=name)
            name  = news.name
            msg_html = render_to_string('email.html', {'news': news})



            for i in Contact.objects.all():

                send_mail(name,'sdfsdfs','ponopaytov@Gmail.com', [i.email] , fail_silently=False, html_message=msg_html)

            return rass

        rass(instance.id, instance.name)




