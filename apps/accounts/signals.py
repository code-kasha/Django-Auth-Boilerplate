from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User, Profile


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
