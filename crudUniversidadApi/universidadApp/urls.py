from django.conf.urls import url 
from universidadApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^facultad$', views.facultadApi),
    url(r'^facultad/([0-9]+)$', views.facultadApi),

    url(r'^administrativo$',views.administrativoApi),
    url(r'^administrativo/([0-9]+)$',views.administrativoApi),

    url(r'^administrativo/savefile',views.savefile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)