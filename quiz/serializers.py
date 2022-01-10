# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import Alternativa, Exercicio

class ExercicioSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Exercicio
        fields = ['numero', 'url', 'respostaAluno']   
        
        read_only_fields = ['numero', 'respostaAluno']
        
class AlternativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alternativa
        fields = [
            "resposta",
            "texto",
        ]

class ExercicioDetailSerializer(serializers.ModelSerializer):
    
    alternativas = AlternativaSerializer(many=True, read_only = True)

    class Meta:
        model = Exercicio
        fields = [
            "texto",
            "respostaAluno",
            "alternativas",
        ]
        
        read_only_fields = ['texto']
        
    def validate_respostaAluno(self, value):
        if value.strip() == '':
            raise serializers.ValidationError("Resposta é obrigatória!")
        alternativas = Alternativa.objects.filter(exercicio = self.instance)
        achou = False
        for alternativa in alternativas:
            achou = achou or value.upper() == alternativa.resposta.upper()
        if not achou:
            raise serializers.ValidationError("Alternativa inválida")
        return value