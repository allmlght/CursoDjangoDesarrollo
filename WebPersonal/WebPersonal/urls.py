"""WebPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views as core_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home,name="home"),
    path('about/',core_views.about,name="about"),
    path('contact/',core_views.contact,name="contact"),
    path('proyectos/',core_views.proyectos,name="proyectos"),
    path('maos/',core_views.maos,name="proyecto"),
    path('auri/',core_views.auri,name="proyecto"),
    path('casabuin/',core_views.casabuin,name="proyecto"),
    path('casalinas/',core_views.casalinas,name="proyecto"),
    path('cabanas/',core_views.cabanas,name="proyecto"),
    path('cajon/',core_views.cajon,name="proyecto"),
    path('servicios/',core_views.servicios,name="proyecto"),
    path('mensajecontacto/',core_views.mensajecontacto,name="about"),
]
