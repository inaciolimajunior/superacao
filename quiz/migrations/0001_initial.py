# Generated by Django 4.0.1 on 2022-01-08 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.aluno')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.exercicio')),
                ('resposta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.alternativa')),
            ],
        ),
        migrations.AddField(
            model_name='alternativa',
            name='exercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.exercicio'),
        ),
    ]
