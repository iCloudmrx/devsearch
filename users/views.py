from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile(request,pk):
    user_profile=Profile.objects.get(id=pk)
    return render(request,'users/profile.html',{
        'profile':user_profile
    })