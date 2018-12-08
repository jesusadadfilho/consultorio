from django.db import models

class Especialidade(models.Model):

     nome = models.CharField(max_length=30)
     descricao = models.CharField(max_length=100)


class Medico(models.Model):
    nome = models.CharField(max_length=30)
    CPF = models.CharField(max_length=14)
    dt_nascimento = models.DateField()
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,
                                      related_name="medicos")


class Atendente(models.Model):

    nome = models.CharField(max_length=30)
    CPF =  models.CharField(max_length=14)
    dt_nascimento = models.DateField()


class Cliente(models.Model):

    nome = models.CharField(max_length=30)
    CPF = models.CharField(max_length=14)
    dt_nascimento = models.DateField()
    SEXO = (
        ('M', 'masculino'),
        ('F', 'feminino')
    )
    sexo = models.CharField(max_length=1, choices=SEXO)


class Agendamento(models.Model):

    dt_agendamento = models.DateTimeField()
    dt_agendada = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, related_name='agendamentos',
                                on_delete=models.CASCADE)
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE,
                                  related_name="agendamentos")
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,
                                      related_name="agendamentos")


class Consulta(models.Model):

    dt_consulta = models.DateTimeField()
    diagnostico = models.CharField(max_length=100)
    agendamento = models.OneToOneField(Agendamento, null=True,
                                       on_delete=models.SET_NULL,
                                       related_name="Consulta")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,
                                related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,
                               related_name="consultas")

