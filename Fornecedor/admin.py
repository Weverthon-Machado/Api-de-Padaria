from django.contrib import admin

from Fornecedor.models import Fornecedor

class Fornecedors(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'telefone', 'email', 'endereco', 'codigo_fonecedor', 'produto')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Fornecedor, Fornecedors)