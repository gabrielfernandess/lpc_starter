"""lpc_starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from evento.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^eventos/$', listaEvento, name='listaEvento'),
    url(r'^eventosCientificos/$', listaEventoCientifico, name='listaEventoCientifico'),
    url(r'^artigoCientifico/$', listaArtigoCientifico, name='listaArtigoCientifico'),
    url(r'^pessoas/$', listaPessoa, name='listaPessoa'),
    url(r'^autores/$', listaAutor, name='listaAutor'),
    

]
