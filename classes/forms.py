from django.forms import ModelForm, TextInput, DateInput
from .models import Especialidade, Medico, Cliente, Atendente, Agendamento, Consulta


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
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do Médico"}),
            'CPF': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite o CPF do Médico"}),
            'dt_nascimento': DateInput(attrs={'type': "date"}),
        }


class PacienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do Paciente"}),
            'CPF': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite o CPF do paciente"}),
            'dt_nascimento': DateInput(attrs={'type': "date"}),
        }


class AtendenteForm(ModelForm):

    class Meta:
        model = Atendente
        fields = '__all__'

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do Paciente"}),
            'CPF': TextInput(attrs={'class': 'form-control', 'placeholder': "Digite o CPF do paciente"}),
            'dt_nascimento': DateInput(attrs={'type': "date"}),
        }


class AgendamentoForm(ModelForm):

    class Meta:
        model = Agendamento
        exclude = ['dt_agendamento']

        widgets = {
            'dt_agendada': DateInput(attrs={'type': "date"}),
            'dt_agendamento': DateInput(attrs={'type': "date"}),
        }


class ConsultaForm(ModelForm):

    class Meta:
        model = Consulta
        exclude = ['dt_consulta']

        widgets = {
            'dt_agendada': DateInput(attrs={'type': "date"}),
            'dt_agendamento': DateInput(attrs={'type': "date"}),
        }