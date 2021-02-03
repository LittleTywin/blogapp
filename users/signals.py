from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings

from .models import Profile

import os

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_delete, sender=Profile)
def delete_media(sender, instance, **kwargs):
    if instance.image.url!=settings.DEFAULT_PROF_IMG_URL:
        try:
            os.remove(instance.image.path)
        except:
            pass


