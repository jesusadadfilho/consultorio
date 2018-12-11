from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_especialidades')
    else:
        form = EspecialidadeForm()
        return render(request, 'nova_especialidade.html',
                      {'form': form})


def editar_especialidade(request, id):
    especialidade = get_object_or_404(Especialidade, id=id)

    if request.method == "POST":
        form = EspecialidadeForm(request.POST, instance=Especialidade)
        if form.is_valid():
            form.save()
        return redirect('mostrar_especialidades')
    else:
        form = EspecialidadeForm(instance=especialidade)
        return render(request, 'nova_especialidade.html',
                  {'form': form})


def remover_especialidade(request, id):
    Especialidade.objects.get(id=id).delete()
    return redirect('mostrar_especialidades')


def mostrar_consultas(request):
    pass


def mostrar_pacientes(request):
    pacientes = Cliente.objects.all()
    return render(request, 'pacientes.html',
                  {'pacientes': pacientes})


def novo_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_pacientes')
    else:
        form = PacienteForm()
        return render(request, 'novo_paciente.html',
                      {'form': form})

def novo_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_medicos')
    else:
        form = MedicoForm()
        return render(request, 'novo_medico.html',
                      {'form': form})


def mostrar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos.html',
                  {'medicos': medicos})


def mostrar_atendentes(request):
    atendentes = Atendente.objects.all()
    return render(request, 'atendente.html',
                  {'atendentes': atendentes})


def novo_atendente(request):
    if request.method == "POST":
        form = AtendenteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_atendentes')
    else:
        form = AtendenteForm()
        return render(request, 'novo_atendente.html',
                      {'form': form})
