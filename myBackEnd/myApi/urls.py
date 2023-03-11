from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskApiView.as_view()),
]