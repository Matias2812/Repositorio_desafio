from django.urls import path
from usuarios.views import inicio,lista_familiares,alta_familiares

urlpatterns=[
    
    path('inicio/', inicio),
    path('familia/', lista_familiares),
    path('familiares/',alta_familiares)


]