from django.urls import path
from usuarios.views import inicio,lista_familiares,alta_familiares, curso, alta_curso

urlpatterns=[
    
    path('inicio/', inicio),
    path('familia/', lista_familiares),
    path('familiares/',alta_familiares),
    path('cursos', curso),
    path('otro_curso/<nombre>', alta_curso)


]