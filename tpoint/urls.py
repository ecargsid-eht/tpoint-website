from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.conf.urls import include
from datawork.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('c-prog',cProg,name='cprog'),
    path('accounts/', include('allauth.urls')),
    path('procourse/<int:id>/<slug:slug>',proCourse,name='procourse')
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
