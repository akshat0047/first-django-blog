from django.contrib import admin
from django.urls import path
from . import views as v

app_name = "articles"

urlpatterns = [
     path('', v.home, name="home"),
     path('post/<int:pk>/', v.details, name="details"),
     path('create/', v.carticle, name="carticle")
     ]
