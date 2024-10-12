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
