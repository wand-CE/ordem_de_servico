from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

SEXO_OPCOES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outro"),
]


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=4)
    cep = models.CharField(max_length=9)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cep}'


class Telefone(models.Model):
    TIPO_TELEFONE = [
        ("FIXO", "fixo"),
        ("CELULAR", "celular"),
    ]
    numero = models.CharField(max_length=11)
    tipo = models.CharField(max_length=7, choices=TIPO_TELEFONE)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return self.numero


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_OPCOES, )
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    # telefones = models.ManyToManyField(Telefone)
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


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


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


class ContaReceber(models.Model):
    ordem_servico = models.ForeignKey(ItemOrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Conta a Receber'
        verbose_name_plural = 'Contas a Receber'

    def __str__(self):
        return f'{self.ordem_servico} a ser recebido'


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
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
        verbose_name_plural = 'Telefones Empresa'


class TelefoneFornecedor(Telefone):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='telefones_fornecedor')

    class Meta:
        verbose_name = 'Telefone Fornecedor'
        verbose_name_plural = 'Telefones Fornecedor'


class TelefoneFuncionario(Telefone):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='telefones_funcionario')

    class Meta:
        verbose_name = 'Telefone Funcionario'
        verbose_name_plural = 'Telefones Funcionario'
