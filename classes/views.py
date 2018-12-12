from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


def mostrar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos.html',
                  {'agendamentos': agendamentos})


def novo_agendamento(request):
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agend = form.save(commit=False)
            agend.dt_agendamento = datetime.now()
            agend.save()
        return redirect('mostrar_agendamentos')
    else:
        form = AgendamentoForm()
        return render(request, 'novo_agendamento.html',
                      {'form': form})


def remover_agendamento(request, id):
    Agendamento.objects.get(id=id).delete()
    return redirect('mostrar_agendamentos')


def mostrar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas.html',
                  {'consultas': consultas})


def nova_consulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            cosulta = form.save(commit=False)
            cosulta.dt_consulta = cosulta.agendamento.dt_agendada
            cosulta.save()
        return redirect('mostrar_consultas')
    else:
        form = ConsultaForm()
        return render(request, 'nova_consulta.html',
                      {'form': form})


def remover_consulta(request, id):
    Consulta.objects.get(id=id).delete()
    return redirect('mostrar_consultas')


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
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('mostrar_especialidades')
        else:
            form = EspecialidadeForm(instance=especialidade)
            return render(request, 'nova_especialidade.html',
                          {'form': form})
    else:
        form = EspecialidadeForm(instance=especialidade)
        return render(request, 'nova_especialidade.html',
                  {'form': form})


def remover_especialidade(request, id):
    Especialidade.objects.get(id=id).delete()
    return redirect('mostrar_especialidades')


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


def editar_paciente(request, id):
    paciente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('mostrar_pacientes')
        else:
            form = PacienteForm(instance=paciente)
            return render(request, 'novo_paciente.html',
                          {'form': form})
    else:
        form = PacienteForm(instance=paciente)
        return render(request, 'novo_paciente.html',
                  {'form': form})


def remover_paciente(request, id):
    Cliente.objects.get(id=id).delete()
    return redirect('mostrar_pacientes')


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

def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)

    if request.method == "POST":
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('mostrar_medicos')
        else:
            form = MedicoForm(instance=medico)
            return render(request, 'novo_medico.html',
                          {'form': form})
    else:
        form = MedicoForm(instance=medico)
        return render(request, 'novo_medico.html',
                  {'form': form})



def mostrar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos.html',
                  {'medicos': medicos})


def remover_medico(request, id):
    medico = Medico.objects.get(id=id).delete()
    return redirect('mostrar_medicos')


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


def remover_atendente(request, id):
    Atendente.objects.get(id=id).delete()
    return redirect('mostrar_atendentes')
