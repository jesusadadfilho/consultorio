
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
]
