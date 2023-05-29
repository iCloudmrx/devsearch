from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class Project(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    featured_image=models.ImageField(blank=True,null=True,default='default.jpg')
    vote_total=models.IntegerField(default=0,blank=True,null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    source_link=models.CharField(blank=True, null=True,max_length=255)
    demo_link = models.CharField(blank=True, null=True,max_length=255)
    tags=models.ManyToManyField("Tag", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    # owner=
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    VOTE_TYPE=(
        ('up', 'up vote'),
        ('down', 'down vote')
    )
    body=models.TextField(blank=True,null=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name=models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name