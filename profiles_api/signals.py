# To automatically create a Profile when a User is created, you can use Django signals. Specifically, the post_save signal can be used to create a Profile instance every time a User instance is saved.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: #create a new profile whe a new user is created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() # saves the profile whenever the user is saved (like after an update)