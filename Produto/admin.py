from django.contrib import admin

from Produto.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao','codigo_produto', 'valor_de_custo','valor_de_venda', 'quantidade_estoque', 'fornecedor', 'fabricante')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Produto, Produtos)