from django.core.validators import RegexValidator
from django.db import models

SEXO_OPCOES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outros"),
]


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=4)
    cep = models.CharField(max_length=9)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Telefone(models.Model):
    TIPO_TELEFONE = [
        ("FIXO", "fixo"),
        ("CELULAR", "celular"),
    ]
    numero = models.CharField(max_length=11)  # definir depois tamanho máximo e validator
    tipo = models.CharField(max_length=7, choices=TIPO_TELEFONE)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_OPCOES)
    nascimento = models.DateTimeField()
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    telefone = models.ManyToManyField(Telefone)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.ManyToManyField(Telefone)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Escolaridade(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridades'


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_OPCOES)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    telefone = models.ManyToManyField(Telefone)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


class OrdemServico(models.Model):
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Ordem de serviço'
        verbose_name_plural = 'Ordens de serviço'


class ItemOrdemServico(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item da ordem de serviço"
        verbose_name_plural = "Itens das ordens de serviço"


class ContaReceber(models.Model):
    ordem_servico = models.ForeignKey(ItemOrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Conta a Receber'
        verbose_name_plural = 'Contas a Receber'


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    email = models.EmailField()
    telefones = models.ManyToManyField(Telefone)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
