from django.db import models

from gerenciador_base_app.models import Telefone, Endereco


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class TelefoneFornecedor(Telefone):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='telefones_fornecedor')

    class Meta:
        verbose_name = 'Telefone Fornecedor'
        verbose_name_plural = 'Telefones Fornecedor'


class EnderecoFornecedor(Endereco):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='enderecos_fornecedor')

    class Meta:
        verbose_name = 'Endereço Fornecedor'
        verbose_name_plural = 'Endereços Fornecedor'
