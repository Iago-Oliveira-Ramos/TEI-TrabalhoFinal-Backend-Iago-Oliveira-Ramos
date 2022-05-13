from rest_framework import serializers
from EmpregadoApp.models import Departamentos, Empregados, Usuarios

class DepartamentoSerializer(serializers.ModelSerializer):
  class Meta:
    model=Departamentos
    fields=('DepartamentoId', 'DepartamentoNome')

class EmpregadoSerializer(serializers.ModelSerializer):
  class Meta:
    model=Empregados
    fields=('EmpregadoId', 'EmpregadoNome', 'Departamento', 'DataDeIngressao', 'FotoPerfil')

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model=Usuarios
    fields=('UsuarioId', 'Login', 'Senha')
