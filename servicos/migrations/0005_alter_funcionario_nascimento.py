# Generated by Django 5.1.1 on 2024-10-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_alter_funcionario_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
