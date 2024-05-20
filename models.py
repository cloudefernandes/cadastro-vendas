from django.db import models

class Clientes(models.Model):
    id_clientes = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    telefone = models.TextField(max_length=50)



class Vendas(models.Model):
    id_vendas = models.AutoField(primary_key=True)
    data = models.DateField()
    produto = models.TextField(max_length=50)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.TextField(max_length=50)

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

    