
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.CharField(max_length=256, blank=True, null=True, default=None)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance )



@receiver
def save_user_profile(sender, inctance, **kwargs):
    inctance.profile.save()





