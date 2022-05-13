from django.db import models

# Create your models here.

class Departamentos(models.Model):
  DepartamentoId = models.AutoField(primary_key=True)
  DepartamentoNome = models.CharField(max_length=500)

class Empregados(models.Model):
  EmpregadoId = models.AutoField(primary_key=True)
  EmpregadoNome = models.CharField(max_length=500)
  Departamento = models.CharField(max_length=500)
  DataDeIngressao = models.DateField()
  FotoPerfil = models.CharField(max_length=500)

class Usuarios(models.Model):
  UsuarioId = models.AutoField(primary_key=True)
  Login = models.CharField(max_length=500)
  Senha = models.CharField(max_length=500)
