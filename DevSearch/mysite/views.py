from django.shortcuts import render
from users.models import Profile
from users.utils import searchProfile
from projects.utils import paginateObjects

def home(request):
    profiles, search_query = searchProfile(request)
    profiles,custom_range=paginateObjects(request,profiles,3)
    print(profiles)
    print(search_query)
    return render(request, 'index.html', {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range':custom_range
    })