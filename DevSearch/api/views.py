from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

# Create your views here.
@api_view(['GET'])
def getProjects(request):
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    projects=Project.objects.get(id=pk)
    serializer=ProjectSerializer(projects,many=False)
    return Response(serializer.data)