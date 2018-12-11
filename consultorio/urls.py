
from django.contrib import admin
from django.urls import path
from classes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agendamentos/', views.mostrar_agendamentos, name='mostrar_agendamentos'),
    path('especialidades/', views.mostrar_especialidades, name='mostrar_especialidades'),
    path('consultas/', views.mostrar_consultas, name='mostrar_consultas'),
    path('pacientes/', views.mostrar_pacientes, name='mostrar_pacientes'),
    path('medicos/', views.mostrar_medicos, name='mostrar_medicos'),
    path('atendentes/', views.mostrar_atendentes, name='mostrar_atendentes'),
    path('medicos/novo', views.novo_medico, name='novo_medico'),
    path('atendentes/novo', views.novo_atendente, name='novo_atendente'),
    path('especialidades/novo', views.nova_especialidade, name='nova_especialidade'),
    path('pacientes/novo', views.novo_paciente, name='novo_paciente'),
    path('especialidades/remover/<int:id>', views.remover_especialidade, name='remover_especialidade'),
    path('medicos/remover/<int:id>', views.excluir_medico, name='excluir_medico'),
    path('atendentes/remover/<int:id>', views.remover_atendente, name='remover_atendente'),
    path('pacientes/remover/<int:id>', views.remover_paciente, name='remover_paciente'),
    path('agendamentos/novo', views.novo_agendamento, name='novo_agendamento'),
    path('especialidades/editar/<int:id>', views.editar_especialidade, name='editar_especialidade'),
]
