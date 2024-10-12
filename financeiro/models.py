from django.db import models

from ordens_de_servico.models import ItemOrdemServico


class ContaReceber(models.Model):
    ordem_servico = models.ForeignKey(ItemOrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Conta a Receber'
        verbose_name_plural = 'Contas a Receber'

    def __str__(self):
        return f'{self.ordem_servico} a ser recebido'
