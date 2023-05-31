from django.shortcuts import render
from users.models import Profile

def home(request):
    profiles=Profile.objects.all()
    return render(request,'index.html',{
        'profiles':profiles
    })