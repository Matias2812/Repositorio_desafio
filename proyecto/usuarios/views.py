from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from usuarios.models import Curso
from usuarios.models import Familiares

# Create your views here.

def inicio(request):
    render(request, 'index.html')

def lista_familiares(request):
    familiares= Familiares.objects.all()
    datos= {'datos':familiares}

    return render(request, 'lista_familiares.html', datos)


def alta_familiares(request):
    familiar=Familiares(nombre= 'Ale', edad= 45, fecha= '1976-05-25')
    familiar.save()
    
    familiar = Familiares(nombre= 'Gon', edad= 20, fecha='2002-09-20')
    familiar.save()

    familiar = Familiares(nombre= 'Clau', edad= 60, fecha='1962-11-06')
    familiar.save()
 
    return HttpResponse('Funciona')


def curso(request):
    cursos = Curso.objects.all()
    dicc = {'cursos': cursos}
    plantilla = loader.get_template('curso.html')
    renderizar = plantilla.render(dicc)
    return HttpResponse(renderizar)


def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada='637490')
    curso.save()
    texto = f'Se guardo en la BD el Curso:: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(texto)
