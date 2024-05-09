from django.db import models

class Vendas(models.Model):
    id_vendas = models.AutoField(primary_key=True)
    data = models.DateField()
    produto = models.TextField(max_length=50)
    cliente = models.TextField(max_length=50)

