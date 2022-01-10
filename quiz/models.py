# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import  RichTextField


# Create your models here.
class Exercicio(models.Model):
    numero = models.IntegerField(verbose_name=u"Número")
    titulo = models.CharField(max_length=200, verbose_name=u"Título")
    nivel = models.IntegerField(verbose_name=u"Nível")
    texto = RichTextField(blank= True, verbose_name=u"Texto")
    respostaAluno = models.CharField(max_length=3, verbose_name=u"Resposta", null = True, blank = False)
    
    def __str__(self):
        return "%d %s" % (self.numero , self.titulo)
    
    class Meta:
        ordering = ['numero']
        verbose_name = u"Exercício"
        verbose_name_plural = u"Exercício"
        
class Alternativa(models.Model):
    resposta  = models.CharField(max_length=3, verbose_name=u"Resposta")
    texto = models.CharField(max_length=200, verbose_name=u"Texto")
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='alternativas')
    correta = models.BooleanField(verbose_name=u"Alternativa Correta")

    def __str__(self):
        return self.resposta

    class Meta:
        ordering = ['exercicio', 'resposta']
        verbose_name = u"Alternativa"
        verbose_name_plural = u"Alternativa"