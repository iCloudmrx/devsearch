from django.urls import path
from .views import profile

urlpatterns=[
    path('profile/<str:pk>/',profile,name='user-profile'),
]