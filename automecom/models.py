
from django.contrib.auth.models import User
from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250, default="", blank=True)

    def __str__(self):
        return self.nome[:40]


class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    administrador = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Veiculo(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(max_length=4)
    matricula = models.CharField(max_length=8)

    def __str__(self):
        return self.marca + " " + self.modelo


class Marcacao(models.Model):
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateTimeField()
    descricao = models.CharField()
    estado = models.CharField()

    def __str__(self):
        return f"{self.utilizador.user.username} - {self.data}"
