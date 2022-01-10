# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

# Create your forms here.
class AlternativaFormSet(BaseInlineFormSet):
     def clean(self):
         """Verificar se existem duas respostas iguais"""
         if any(self.errors):
             # Don't bother validating the formset unless each form is valid on its own
             return
         respostas = []
         for form in self.forms:
             if self.can_delete and self._should_delete_form(form):
                 continue
             resposta = form.cleaned_data.get('resposta')
             if resposta in respostas:
                 raise ValidationError(u"Não podem existir duas ou mais respostas iguais")
             respostas.append(resposta)
             
         """Verificar se existem dois textos de respostas iguais"""
         textos = []
         for form in self.forms:
             if self.can_delete and self._should_delete_form(form):
                 continue
             texto = form.cleaned_data.get('texto')
             if texto in textos:
                 raise ValidationError(u"Não podem existir duas ou mais textos de resposta iguais")
             textos.append(texto)
             
         """Apenas Uma alternativa correta"""
         correta = False
         for form in self.forms:
             if self.can_delete and self._should_delete_form(form):
                 continue
             corret_alternativa = form.cleaned_data.get('correta')
             if (correta == True) and (corret_alternativa == True):
                 raise ValidationError(u"Apenas uma alternativa pode ser marcada como correta")
             if correta == False:
                 correta = corret_alternativa
                 
         """Uma alternativa correta deve ser marcada"""
         correta = False
         for form in self.forms:
             if self.can_delete and self._should_delete_form(form):
                 continue
             correta = form.cleaned_data.get('correta') or correta
         if correta == False:
             raise ValidationError(u"Uma alternativa deve ser marcada como correta")
