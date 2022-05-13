from xml.dom.minidom import Document
from django.urls import re_path
from EmpregadoApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
  re_path(r'^departamento$',views.departamentoApi),
  re_path(r'^departamento/([0-9]+)$',views.departamentoApi),

  re_path(r'^empregado$',views.empregadoApi),
  re_path(r'^empregado/([0-9]+)$',views.empregadoApi),

  re_path(r'^usuario$',views.usuarioApi),
  re_path(r'^usuario/([0-9]+)$',views.usuarioApi),

  re_path(r'^empregado/salvarfoto',views.SalvarFoto)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)