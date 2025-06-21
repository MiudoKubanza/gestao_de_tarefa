from django.contrib import admin
from .models import Perfil
# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'bi', 'telefone', 'usuario')
    search_fields = ('nome_completo', 'bi', 'telefone', 'usuario__username')
    ordering = ('nome_completo',)
