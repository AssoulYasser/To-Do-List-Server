from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskApiView.as_view()),
    path('sign-in/', UserSignInApiView.as_view()),
    path('sign-up/', UserSignUpApiView.as_view())
]
