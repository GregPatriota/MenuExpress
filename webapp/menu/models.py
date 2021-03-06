from django.db import models


# Create your models here.
class SimpleProductToSell(models.Model):
    name = models.CharField('Nome do Produto', max_length=128)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2)
