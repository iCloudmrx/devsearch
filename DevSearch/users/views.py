from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Profile, Skill
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import CustomerUserCreationForm,ProfileUpdateForm,SkillCreationForm
from django.contrib.auth.models import User

# Create your views here.


def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("Login")
            return redirect('profiles')
        messages.error(request,'Username or Password is incorrect')
    return render(request,'users/authentication/login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('profiles')

def signup(request):
    if request.method=='POST':
        form=CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            #login(request,user)
            print("Signup")
            return redirect('profiles')
        messages.error(request,'validation of form has error')
    form=CustomerUserCreationForm()
    return render(request,'users/authentication/signup.html',{
        'form':form
    })


def profile(request,pk):
    user_profile = Profile.objects.get(id=pk)
    topSkill = user_profile.skill_set.exclude(description="")
    otherSkill = user_profile.skill_set.filter(description="")
    return render(request,'users/profile.html',{
        'profile': user_profile,
        'tops': topSkill,
        'others': otherSkill
    })

@login_required(login_url='login')
def userAccount(request):
    user_profile=Profile.objects.get(user=request.user)
    skills=user_profile.skill_set.all()
    projects=user_profile.project_set.all()
    return render(request,'users/authentication/account.html',{
        'profile':user_profile,
        'skills':skills,
        'projects':projects
    })

@login_required(login_url='login')
def profileUpdate(request):
    user_profile=request.user.profile
    if request.method=='POST':
        form=ProfileUpdateForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('account')
        messages.error(request,'Server has error')
    form=ProfileUpdateForm()
    return render(request,'users/profile_form.html',{
        'form':form
    })

@login_required(login_url='login')
def skillCreate(request):
    user_profile=request.user.profile
    if request.method=='POST':
        form=SkillCreationForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=user_profile
            skill.save()
            return redirect('account')
        messages.error(request, 'Server has error')
    form=SkillCreationForm()
    return render(request,'skills/create.html',{
        'form':form
    })


@login_required(login_url='login')
def skillUpdate(request,pk):
    skill=Skill.objects.get(id=pk)
    if request.method=='POST':
        form=SkillCreationForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
        messages.error(request, 'Server has error')
    form=SkillCreationForm()
    return render(request,'skills/edit.html',{
        'form':form
    })

@login_required(login_url='login')
def deleteSkill(request,pk):
    skill=Skill.objects.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    return render(request,'skills/delete.html',{
        'skill': skill
    })