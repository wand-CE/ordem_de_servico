from django.db import models
from base_app.models import Endereco, Telefone, SEXO_OPCOES


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_OPCOES, )
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class TelefoneCliente(Telefone):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefones_cliente')

    class Meta:
        verbose_name = 'Telefone Cliente'
        verbose_name_plural = 'Telefones Cliente'
