# Generated by Django 5.1.1 on 2024-10-11 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_remove_empresa_telefones_funcionario_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='telefones',
        ),
        migrations.CreateModel(
            name='TelefoneFornecedor',
            fields=[
                ('telefone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicos.telefone')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones_fornecedor', to='servicos.fornecedor')),
            ],
            options={
                'verbose_name': 'Telefone Fornecedor',
                'verbose_name_plural': 'Telefones Fornecedor',
            },
            bases=('servicos.telefone',),
        ),
    ]
