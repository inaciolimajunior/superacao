# Generated by Django 4.0.1 on 2022-01-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_remove_exercicio_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='respostaAluno',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Resposta'),
        ),
    ]
