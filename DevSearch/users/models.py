import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    short_intro=models.CharField(max_length=255,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    #skills=models.ManyToManyField('Skill',)
    profile_image=models.ImageField(upload_to='profiles/',default='profiles/user-default.png',null=True,blank=True)
    social_github=models.CharField(max_length=255,null=True,blank=True)
    social_twitter = models.CharField(max_length=255, null=True, blank=True)
    social_linkedin = models.CharField(max_length=255, null=True, blank=True)
    social_youtube = models.CharField(max_length=255, null=True, blank=True)
    social_instagram = models.CharField(max_length=255, null=True, blank=True)
    social_whatsapp = models.CharField(max_length=255, null=True, blank=True)
    social_website = models.CharField(max_length=255, null=True, blank=True)
    social_telegram = models.CharField(max_length=255, null=True, blank=True)
    phone=models.CharField(max_length=255, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

class Skill(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True,related_name='messages')
    name=models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering=['is_read','-created']


    @property
    def is_read_true(self):
        if self.is_read==False:
            self.is_read=True
            self.save()