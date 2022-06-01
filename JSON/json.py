import requests
import os
import zipfile as zip
import pathlib

departamentos = requests.get('http://127.0.0.1:8000/departamento')
empregados = requests.get('http://127.0.0.1:8000/empregado')
usuarios = requests.get('http://127.0.0.1:8000/usuario')



with open('JSON/data/departamentos.txt', 'w') as dep:
  dep.write(departamentos.text)

with open('JSON/data/empregados.txt', 'w') as emp:
  emp.write(empregados.text)

with open('JSON/data/usuarios.txt', 'w') as usu:
  usu.write(usuarios.text)


path_zip = os.path.join(
  os.sep,"C:\\","Users","Iago Ramos","Desktop","django_api","DjangoAPI","DadosDaAplicacao.zip"
)

path_dir = os.path.join(
  os.sep,"C:\\","Users","Iago Ramos","Desktop","django_api","DjangoAPI","JSON","data"
)

files = pathlib.Path(path_dir).rglob('*.txt')

zf = zip.ZipFile(path_zip,"w")

for file in files:
    zf.write(file,file.name)

zf.close()