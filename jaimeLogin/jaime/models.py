# yourapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastseen = models.DateTimeField(null=True, blank=True)



@receiver(post_save, sender=User)
def create_or_update_user_profile(instance, created):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
