from django.db.models import Q
from .models import Project,Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateObjects(request,objects,result):

    paginator=Paginator(objects,result)

    try:
        page=request.GET.get('page',1)
        objects = paginator.page(page)
    except PageNotAnInteger:
        page=1
        objects = paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        objects = paginator.page(page)

    leftIndex=(int(page)-4)

    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+5)

    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1

    custom_range=range(leftIndex,rightIndex)

    return objects,custom_range



def searchProject(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    tag=Tag.objects.filter(name__icontains=search_query)
    print(search_query)
    projects=Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tag)
    )
    return projects,search_query