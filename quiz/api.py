from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Exercicio, Alternativa
from .serializers import ExercicioSerializer, ExercicioDetailSerializer


class ExercicioViewSet(viewsets.ModelViewSet):
    
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioDetailSerializer
    
    def list(self, request):
        queryset = Exercicio.objects.all()
        
        total_questoes = 0
        total_acertos = 0
        total_erros = 0
        
        exercicios = Exercicio.objects.all()
        for exerc in exercicios:
            total_questoes = total_questoes + 1;
            respostaAluno = exerc.respostaAluno 
            if respostaAluno:
               correta = Alternativa.objects.get(correta = True, exercicio = exerc)
               if respostaAluno.upper() == correta.resposta.upper():
                   total_acertos = total_acertos + 1
               else:
                   total_erros = total_erros + 1
                
        aproveitamento = "%d%%" % (int((total_acertos / total_questoes) * 100)) 

        custom_data = [
            {'Total de acertos': total_acertos},
            {'Total de erros' : total_erros},
            {'Aproveitamento' : aproveitamento}
        ]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ExercicioSerializer(page, many=True, context={'request' : request})
            return self.get_paginated_response(serializer.data)

        serializer = ExercicioSerializer(queryset, many=True, context={'request' : request})
        
        data = serializer.data
        retorno = data + custom_data
        
        return Response(retorno)