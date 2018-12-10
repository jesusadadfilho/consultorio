from django.db import models

class Especialidade(models.Model):
     nome = models.CharField(max_length=30)
     descricao = models.CharField(max_length=100)

class Atendente(models.Model):
    nome =  models.CharField(max_length=30)
    dt_nascimento = models.DateField()
    CPF =  models.CharField(max_length=30)

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    dt_nascimento = models.DateField()
    CPF = models.CharField(max_length=30)
    sexo = (
        ('M', 'masculino'),
        ('F', 'feminino')
    )
    sexo = models.CharField(max_length=1, choices=sexo)


class Medico(models.Model):
    nome = models.CharField(max_length=30)
    dt_nascimento = models.DateField()
    CPF = models.CharField(max_length=30)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,related_name="medicos")

class Agendamento(models.Model):
    dt_agendamento = models.DateField()
    dt_agendada = models.DateField()
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE,related_name="agendamentos")
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE,related_name="agendamentos")

class Consulta(models.Model):
    dt_consulta = models.DateField
    agendamento =  models.OneToOneField(Agendamento, on_delete=models.CASCADE,related_name="Consulta")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name="consultas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,related_name="consultas")
    retorno = models.ManyToManyField("self")


