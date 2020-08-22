from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'), name='api'),
    path('articles/', include('apps.articles.urls'), name='articles'),
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('', include('apps.home.urls'), name='home')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
