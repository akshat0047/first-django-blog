from django.contrib import admin
from django.urls import path
from . import views as v

app_name = "articles"

urlpatterns = [
     path('', v.article_list, name="article_list"),
     path('<int:pk>/', v.article_detail, name="article_detail"),
     path('create/', v.article_create, name="article_create"),
     path('delete/<int:item_id>/', v.article_delete, name='article_delete'),
     path("preview/",v.preview_markdown, name="preview_markdown"),
     ]
