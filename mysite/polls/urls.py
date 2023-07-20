from django.urls import path
#path é o caminho

from . import views
#traz oq tiver na view

#quero criar padroes de url e um deles é:
#vazio que ta associado a views index (oq tiver definido de index)
#e vamos chamar isso de index
urlpatterns = [
    path("",views.index, name='index'),
]

#queremos incluir essa url no nosso site
#va para