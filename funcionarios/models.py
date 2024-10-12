from django.contrib.auth.models import User
from django.db import models

from gerenciador_base_app.models import Endereco, SEXO_OPCOES, Telefone


class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome


class Escolaridade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_OPCOES)
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class TelefoneFuncionario(Telefone):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='telefones_funcionario')

    class Meta:
        verbose_name = 'Telefone Funcionario'
        verbose_name_plural = 'Telefones Funcionario'
