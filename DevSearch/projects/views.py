from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .utils import searchProject,paginateObjects
from users.models import Profile
from .models import Project
from .forms import ProjectForm,ReviewForm

# Create your views here.

def createProject(request):
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)

            project.owner=Profile.objects.get(user=request.user)
            project.save()
            return redirect('account')
    form = ProjectForm()
    return render(request,'projects/project-form.html',{
                      'form':form
                  })
def projects(request):
    projectsObj,search_query=searchProject(request)

    projectsObj,custom_range=paginateObjects(request,projectsObj,3)



    return render(request,'projects/project.html',{
        'projects':projectsObj,
        'search_query':search_query,
        'custom_range':custom_range
    })

def singleProjects(request,pk):
    project=Project.objects.get(id=pk)
    review_form=ReviewForm()

    if request.user.is_authenticated:
        if request.method=='POST':
            review_form=ReviewForm(request.POST)
            review=review_form.save(commit=False)
            review.project=project
            review.owner=request.user.profile
            review.save()

            project.getVoteCount

            messages.success(request,'Your review was successfully submitted!')
            return redirect('single-project',pk=project.id)
    else:
        messages.error(request,'You have not done login or signup')


    return render(request,'projects/single-project.html',{
        'project':project,
        'review_form': review_form
    })

@login_required(login_url='login')
def updateProjects(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    return render(request, 'projects/project-form.html', {
        'form': form
    })


@login_required(login_url='login')
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    return render(request,'projects/delete_project.html',{
        'project': project
    })