# -*- coding:utf-8 -*-
from string import ascii_lowercase

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .models import Exercicio, Alternativa


# Create your tests here.
class SuperacaoTestCase(APITestCase):
    
    list_url = reverse("exercicio-list")

    def setup_exercicios(self):
        for i in range(10):
            j = i + 1
            exercicio = Exercicio()
            exercicio.numero = j
            exercicio.titulo = "TITULO %d" % j
            exercicio.nivel = 1
            exercicio.texto = "EXERCICIO %d" % j
            exercicio.save()
            
            for j in range(4):
                alternativa = Alternativa()
                a = list(ascii_lowercase)
                
                alternativa.resposta = a[j]
                alternativa.texto = 'ALTERNATIVA %d' % j
                alternativa.exercicio = exercicio
                alternativa.correta = j == 0 #Alternativa A sempre será a correta
                
                alternativa.save() 
        
    def test_exercicios_listar(self):
        self.setup_exercicios()
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)        
        
    def test_resposta_certa(self):
        self.setup_exercicios()
        
        data = {"respostaAluno": "a"}
        response = self.client.put(reverse("exercicio-detail", kwargs = {"pk": 1}), data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    def test_resposta_errada(self):
        self.setup_exercicios()
        
        data = {"respostaAluno": "b"}
        response = self.client.put(reverse("exercicio-detail", kwargs = {"pk": 2}), data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    def test_resposta_invalida(self):
        self.setup_exercicios()
        
        data = {"respostaAluno": "e"}
        response = self.client.put(reverse("exercicio-detail", kwargs = {"pk": 3}), data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_resposta_embranco(self):
        self.setup_exercicios()
        
        data = {"respostaAluno": "e"}
        response = self.client.put(reverse("exercicio-detail", kwargs = {"pk": 3}), data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
