from django.shortcuts import render
from core.models import *

from django.shortcuts import render, redirect
from django.views.generic.base import View
from core.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

# PARTE EXTERNA (MATRICULAR-SE E LOGIN)

def index(request):
    contexto = {
        'cursos': Curso.objects.all()
            
    } #Esse comando puxa as inf. do BD e printa na página
    return render(request,"index.html",contexto)


def matricula(request):
    form = None
    form = MatriculaForm(request.POST)
    if request.POST:
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login.html")
    else:
        form = MatriculaForm()
    return render(request,"matricula.html")


def login(request):
    return render(request,"logn.html")




# DEPOIS DE LOGAR - PROFESSOR -
def checa_professor(user):
     return user.perfil == 'A'

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def pagina_inicial_professor(request):
    return render(request,"Professor/pagina_inicial.html")


@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def subir_aula(request):
    return render(request,"Professor/subir_aula.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def boletim(request):
    return render(request,"Professor/boletim.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def notas(request):
    return render(request,"Professor/notas.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def seleciona_turma_falta(request):
    return render(request,"Professor/seleciona_turma_falta.html")

@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def faltas(request):
    return render(request,"Professor/faltas.html")



    


