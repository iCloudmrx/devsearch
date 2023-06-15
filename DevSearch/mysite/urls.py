"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/reset/password/',auth_views.PasswordResetView.as_view(template_name='users/reset/reset_password.html'),
         name='reset_password'),

    path('accounts/reset/password/sent/',auth_views.PasswordResetDoneView.as_view(template_name='users/reset/reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/reset/reset.html'),
         name='password_reset_confirm'),

    path('accounts/reset/password/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/reset/complete.html'),
         name='password_reset_complete'),

]+i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n')),
    path('', home, name='profiles'),
    path('api/', include('api.urls')),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
)

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns+=[
#         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
#     ]

handler404='mysite.views.handle_404'