from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from user.models import Profile, CareerProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, **kwargs):
    Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def create_career_profile(sender, instance=None, **kwargs):
    CareerProfile.objects.get_or_create(user=instance)


@receiver(pre_save, sender=User)
def create_career_profile(sender, instance=None, **kwargs):
    instance.email = instance.username
