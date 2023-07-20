from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#criando a visualizacao da pagina inicial
def index(request):
    return HttpResponse("ola")

#preciamos atrelar essa visualizacao a uma url
#va para urls.py dentro de polls