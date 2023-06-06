from django.urls import path
from .views import (getProject,
                    getProjects,
                    projectVote,
                    removeTag
                    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/',getProjects),
    path('project/<str:pk>/',getProject),
    path('project/<str:pk>/vote/', projectVote),
    path('remove/tag/',removeTag)
]