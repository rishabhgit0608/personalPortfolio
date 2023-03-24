from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.home)
]
urlpatterns+= staticfiles_urlpatterns()
