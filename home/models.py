from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    missao = models.TextField()
    visao = models.TextField()
    valores = models.TextField()

    def __str__(self):
        return self.nome