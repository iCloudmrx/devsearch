from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project,Review,Tag


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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project=Project.objects.get(id=pk)
    user=request.user.profile
    data=request.data
    review,created=Review.objects.get_or_create(
        owner=user,
        project=project
    )
    review.value=data['value']
    review.save()
    project.getVoteCount
    print("Data:",data)
    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId=request.data['tagId']
    projectId = request.data['projectId']
    tag=Tag.objects.get(id=tagId)
    project=Project.objects.get(id=projectId)
    project.tags.remove(tag)
    return Response("Tag was deleted")