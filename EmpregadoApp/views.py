from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmpregadoApp.models import Departamentos, Empregados, Usuarios
from EmpregadoApp.serializers import DepartamentoSerializer, EmpregadoSerializer, UsuarioSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def departamentoApi(request, id = 0):
  if request.method == 'GET':
    departamentos = Departamentos.objects.all()
    departamentos_serializer = DepartamentoSerializer(departamentos,many=True)
    return JsonResponse(departamentos_serializer.data, safe=False)

  elif request.method == 'POST':
    departamento_data = JSONParser().parse(request)
    departamentos_serializer = DepartamentoSerializer(data=departamento_data)
    if departamentos_serializer.is_valid():
      departamentos_serializer.save()
      return JsonResponse("Adicionado com sucesso.",safe=False)
    return JsonResponse("Falha ao adicionar departamento.", safe=False)

  elif request.method == 'PUT':
    departamento_data = JSONParser().parse(request)
    departamento = Departamentos.objects.get(DepartamentoId = departamento_data['DepartamentoId'])
    departamentos_serializer = DepartamentoSerializer(departamento, data = departamento_data)
    if departamentos_serializer.is_valid():
      departamentos_serializer.save()
      return JsonResponse("Atualizado com sucesso.", safe=False)
    return JsonResponse("Falha ao atualizar departamento.", safe=False)

  elif request.method == 'DELETE':
    departamento = Departamentos.objects.get(DepartamentoId = id)
    departamento.delete()
    return JsonResponse("Departamento deletado com sucesso.", safe=False)
  

@csrf_exempt
def empregadoApi(request, id = 0):
  if request.method == 'GET':
    empregados = Empregados.objects.all()
    empregados_serializer = EmpregadoSerializer(empregados,many=True)
    return JsonResponse(empregados_serializer.data, safe=False)

  elif request.method == 'POST':
    empregado_data = JSONParser().parse(request)
    empregados_serializer = EmpregadoSerializer(data=empregado_data)
    if empregados_serializer.is_valid():
      empregados_serializer.save()
      return JsonResponse("Adicionado com sucesso.",safe=False)
    return JsonResponse("Falha ao adicionar empregado.", safe=False)

  elif request.method == 'PUT':
    empregado_data = JSONParser().parse(request)
    empregado = Empregados.objects.get(EmpregadoId = empregado_data['EmpregadoId'])
    empregados_serializer = EmpregadoSerializer(empregado, data = empregado_data)
    if empregados_serializer.is_valid():
      empregados_serializer.save()
      return JsonResponse("Atualizado com sucesso.", safe=False)
    return JsonResponse("Falha ao atualizar empregado.", safe=False)

  elif request.method == 'DELETE':
    empregado = Empregados.objects.get(EmpregadoId = id)
    empregado.delete()
    return JsonResponse("Empregado deletado com sucesso.", safe=False)

@csrf_exempt
def usuarioApi(request, id = 0):
  if request.method == 'GET':
    usuarios = Usuarios.objects.all()
    usuarios_serializer = UsuarioSerializer(usuarios,many=True)
    return JsonResponse(usuarios_serializer.data, safe=False)

  elif request.method == 'POST':
    usuario_data = JSONParser().parse(request)
    usuarios_serializer = UsuarioSerializer(data=usuario_data)
    if usuarios_serializer.is_valid():
      check_Existing = Usuarios.objects.filter(Login=usuario_data['Login']) and Usuarios.objects.filter(Senha=usuario_data['Senha']).exists
      if check_Existing:
        return JsonResponse("Usuário já existe com esse nome!",safe=False)
      usuarios_serializer.save()
      return JsonResponse("Usuário criado com sucesso.",safe=False)
    return JsonResponse("Falha ao adicionar usuario.", safe=False)

  elif request.method == 'PUT':
    usuario_data = JSONParser().parse(request)
    usuario = Usuarios.objects.get(UsuarioId = usuario_data['UsuarioId'])
    usuarios_serializer = UsuarioSerializer(usuario, data = usuario_data)
    if usuarios_serializer.is_valid():
      usuarios_serializer.save()
      return JsonResponse("Atualizado com sucesso.", safe=False)
    return JsonResponse("Falha ao atualizar usuário.", safe=False)

  elif request.method == 'DELETE':
    usuario = Usuarios.objects.get(UsuarioId = id)
    usuario.delete()
    return JsonResponse("Usuário deletado com sucesso.", safe=False)

@csrf_exempt
def SalvarFoto(request):
  file = request.FILES['file']
  file_name = default_storage.save(file.name, file)
  return JsonResponse(file_name, safe=False)