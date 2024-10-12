from django.db import models

from gerenciador_base_app.models import Endereco, Telefone


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


class TelefoneEmpresa(Telefone):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='telefones_empresa')

    class Meta:
        verbose_name = 'Telefone Empresa'
        verbose_name_plural = 'Telefones Empresas'


class EnderecoEmpresa(Endereco):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='enderecos_empresa')

    class Meta:
        verbose_name = 'Endereço Empresa'
        verbose_name_plural = 'Endereços Empresas'
