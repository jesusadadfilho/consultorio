from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


def mostrar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos.html',
                  {'agendamentos': agendamentos})


def mostrar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades.html',
                  {'especialidades': especialidades})


def nova_especialidade(request):
    form = EspecialidadeForm()
    return render(request, 'nova_especialidade.html',
                  {'form': form})


def mostrar_consultas(request):
    pass


def mostrar_pacientes(request):
    pass


def mostrar_medicos(request):
    pass
