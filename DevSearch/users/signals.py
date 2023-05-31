from django.contrib.auth.models import User

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=f'{user.first_name} {user.last_name}'
        )
@receiver(post_save,sender=Profile)
def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        name=profile.name.split(' ')
        user.username=profile.username
        user.email=profile.email
        user.first_name=name[0]
        user.last_name=name[1]
        user.save()


@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

