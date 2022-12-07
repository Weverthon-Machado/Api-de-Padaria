from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)   
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    matricula = models.IntegerField()
    data_admissao = models.DateField()
    cargo = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome