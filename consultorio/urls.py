
from django.contrib import admin
from django.urls import path
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('especialidades/', views.mostrar_especialidades, name='mostrar_especialidades'),
    path('especialidades/novo', views.nova_especialidade, name='nova_especialidade'),
    path('especialidades/editar/<int:id>', views.editar_especialidade, name='editar_especialidade'),
    path('especialidades/remover/<int:id>', views.remover_especialidade, name='remover_especialidade'),
    path('pacientes/', views.mostrar_pacientes, name='mostrar_pacientes'),
    path('pacientes/novo', views.novo_paciente, name='novo_paciente'),
    path('pacientes/remover/<int:id>', views.remover_paciente, name='remover_paciente'),
    path('medicos/', views.mostrar_medicos, name='mostrar_medicos'),
    path('medicos/novo', views.novo_medico, name='novo_medico'),
    path('medicos/remover/<int:id>', views.remover_medico, name='remover_medico'),
    path('atendentes/', views.mostrar_atendentes, name='mostrar_atendentes'),
    path('atendentes/novo', views.novo_atendente, name='novo_atendente'),
    path('atendentes/remover/<int:id>', views.remover_atendente, name='remover_atendente'),
    path('agendamentos/', views.mostrar_agendamentos, name='mostrar_agendamentos'),
    path('agendamentos/novo', views.novo_agendamento, name='novo_agendamento'),
    path('consultas/', views.mostrar_consultas, name='mostrar_consultas'),
]

