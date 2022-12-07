import email
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)   
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    codigo_cliente = models.IntegerField()

    def __str__(self):
        return self.nome