import email
from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length = 100)
    cnpj = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    email = models.EmailField()
    endereco= models.CharField(max_length = 100)
    codigo_fonecedor = models.IntegerField()
    produto = models.CharField(max_length = 100) 
    
    def __str__(self):
        return self.nome