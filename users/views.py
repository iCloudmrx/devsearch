from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile(request,pk):
    user_profile = Profile.objects.get(id=pk)
    topSkill = user_profile.skill_set.exclude(description="")
    otherSkill = user_profile.skill_set.filter(description="")
    return render(request,'users/profile.html',{
        'profile': user_profile,
        'tops': topSkill,
        'others': otherSkill
    })