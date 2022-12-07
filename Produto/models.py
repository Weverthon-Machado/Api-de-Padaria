from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 300)
    codigo_produto = models.IntegerField()
    valor_de_custo = models.DecimalField(decimal_places=2,max_digits= 4)
    valor_de_venda = models.DecimalField(decimal_places=2,max_digits= 4)
    quantidade_estoque = models.IntegerField()
    fornecedor = models.CharField(max_length = 100)
    fabricante = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome
    