from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField() #auto_now_add=True
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        return self.descricao