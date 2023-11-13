from django.contrib import admin
from .models import Aluno

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula', 'data_inscricao')
    list_filter = ('nome', 'matricula','data_inscricao')


admin.site.register(Aluno, AlunoAdmin)