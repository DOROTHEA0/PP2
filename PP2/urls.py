"""PP2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import mainView
from csc import views
from django.urls import re_path
from django.views.static import serve
from PP2 import settings

urlpatterns = [
    re_path('^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('', mainView.to_main, name='main'),
    path('view_details/(?P<aid>d+)/', mainView.to_meeting_details, name='mt_d'),
    path('view/', mainView.to_meeting, name='mt'),
    path('login/', views.to_login, name='to_login'),
    path('register/', views.to_register, name='to_register'),
    path('l/', views.logout, name='logout'),
    path('upload/', views.to_upload, name='upload'),
]
