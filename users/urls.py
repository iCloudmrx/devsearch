from django.urls import path
from .views import profile,loginPage,logoutPage,signup,userAccount,profileUpdate

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('account/',userAccount,name='account'),
    path('profile/update/',profileUpdate,name='profile-update'),
    path('profile/<str:pk>/',profile,name='user-profile'),
]