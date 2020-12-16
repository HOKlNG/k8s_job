from django.contrib import admin
from django.urls import path, include, re_path
from .views import index,LoginView,UserLoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login/access', UserLoginView.as_view()),
]