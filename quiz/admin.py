# Register your models here.
from django.contrib import admin

from .models import Alternativa, Exercicio
from .forms import AlternativaFormSet


class AlternativaAdminInLine(admin.TabularInline):
    model = Alternativa
    extra = 4
    min_num = 4
    max_num = 4
    can_delete = False
    
    formset = AlternativaFormSet

class ExercicioAdmin(admin.ModelAdmin):
    
    inlines = [AlternativaAdminInLine]
    
    readonly_fields = ['respostaAluno']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        obj_id = request.META['PATH_INFO'].rstrip('/').split('/')[-2]
        if db_field.name == 'respostaAluno' and obj_id.isdigit():
            obj = self.get_object(request, obj_id)
            if obj:
                 kwargs["queryset"] = Alternativa.objects.filter(exercicio = obj)
        if db_field.name == 'respostaAluno' and not obj_id.isdigit():
            kwargs["queryset"] = Alternativa.objects.filter(id = 0)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Exercicio, ExercicioAdmin)