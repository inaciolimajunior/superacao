# Generated by Django 4.0.1 on 2022-01-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_alter_exercicio_options_exercicio_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='respostaAluno',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Resposta'),
        ),
    ]
