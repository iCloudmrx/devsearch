from django.urls import path
from .views import profile,loginPage,logoutPage,signup,userAccount,profileUpdate,skillUpdate,skillCreate,deleteSkill

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('account/',userAccount,name='account'),
    path('profile/update/',profileUpdate,name='profile-update'),
    path('profile/<str:pk>/',profile,name='user-profile'),
    path('skill/create/',skillCreate,name='skill-create'),
    path('skill/update/<str:pk>/',skillUpdate,name='skill-update'),
    path('skill/delete/<str:pk>/',deleteSkill,name='skill-delete'),

]