from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from users.models import Profile
from .models import Project
from .forms import ProjectForm

# Create your views here.

def createProject(request):
    if request.method=='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)

            project.owner=Profile.objects.get(user=request.user)
            project.save()
            return redirect('project')
    form = ProjectForm()
    return render(request,'projects/project-form.html',{
                      'form':form
                  })
def projects(request):
    projectsObj=Project.objects.all()
    return render(request,'projects/project.html',{
        'projects':projectsObj
    })

def singleProjects(request,pk):
    project=Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{
        'project':project
    })

@login_required(login_url='login')
def updateProjects(request,pk):
    project=Project.objects.get(id=pk)
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