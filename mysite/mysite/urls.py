
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #vamos incluir nos padroes os aplicativos no formato polls
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
