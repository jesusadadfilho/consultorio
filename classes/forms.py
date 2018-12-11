from django.forms import ModelForm, TextInput
from .models import Especialidade


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