from django.contrib import admin
from django.urls import path, include, re_path

from .views import index, MyPage

urlpatterns = [
    path('',index),
    path('interface',MyPage.as_view(template_name='interface.html'))

]