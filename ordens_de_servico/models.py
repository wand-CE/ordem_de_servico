from django.db import models

from clientes.models import Cliente
from funcionarios.models import Funcionario
from produtos.models import Produto


class OrdemServico(models.Model):
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Ordem de serviço'
        verbose_name_plural = 'Ordens de serviço'

    def __str__(self):
        return self.descricao


class ItemOrdemServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item da ordem de serviço"
        verbose_name_plural = "Itens das ordens de serviço"

    def __str__(self):
        return f'{self.produto} com valor {self.valor_total}'
