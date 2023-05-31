from django.urls import path
from .views import createProject,projects,singleProjects,updateProjects,deleteProject

urlpatterns=[
    path('', projects, name='project'),
    path('project/<str:pk>/', singleProjects, name='single-project'),
    path('update-project/<str:pk>/', updateProjects, name='update-project'),
    path('project-form/', createProject, name='create-project'),
    path('delete-project/<str:pk>/', deleteProject, name='delete-project'),
]