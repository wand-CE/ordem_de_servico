# Generated by Django 5.1.1 on 2024-10-12 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('funcionarios', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionario')),
            ],
            options={
                'verbose_name': 'Ordem de serviço',
                'verbose_name_plural': 'Ordens de serviço',
            },
        ),
        migrations.CreateModel(
            name='ItemOrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordens_de_servico.ordemservico')),
            ],
            options={
                'verbose_name': 'Item da ordem de serviço',
                'verbose_name_plural': 'Itens das ordens de serviço',
            },
        ),
    ]
