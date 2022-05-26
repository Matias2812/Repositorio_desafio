from django.urls import path
from usuarios import views

urlpatterns=[
    
    path('', views.nueva_pagina),
    path('inicio/', views.inicio),
    path('familia/', views.lista_familiares),
    path('familiares/', views.alta_familiares),
    path('cursos', views.curso, name='curso'),
    path('otro_curso/<nombre>', views.alta_curso),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('contacto/', views.contactos),


]