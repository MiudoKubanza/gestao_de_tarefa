import os
from django.contrib import admin

from gestao_de_tarefas.settings import BASE_DIR
from .models import Tarefa, Categoria
# Register your models here.

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridade', 'concluida', 'data_criacao', 'data_limite', 'usuario')
    list_filter = ('prioridade', 'concluida', 'categoria')
    search_fields = ('titulo', 'descricao')
    ordering = ('-data_criacao',)
    date_hierarchy = 'data_criacao'


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)