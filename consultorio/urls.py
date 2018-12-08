
from django.contrib import admin
from django.urls import path
from classes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agendamentos/', views.mostrar_agendamentos, name='mostrar_agendamentos'),
]
