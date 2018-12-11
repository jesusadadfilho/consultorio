from django.forms import ModelForm, TextInput
from .models import Especialidade, Medico, Cliente


class EspecialidadeForm(ModelForm):

    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome da especialidade"}),
            'descricao': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite uma breve descrição"}),
        }

        error_messages = {
            'nome': {
                'max_length': ("This writer's name is too long."),
            },
        }

class MedicoForm(ModelForm):

    class Meta:
        model = Medico
        fields = '__all__'

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do Paciente"}),
            'CPF': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite o CPF do paciente"}),
            'dt_nascimento': TextInput(attrs={'type': "date"}),
        }

        error_messages = {
            'nome': {
                'max_length': ("This writer's name is too long."),
            },
        }


class PacienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do Paciente"}),
            'CPF': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite o CPF do paciente"}),
        }