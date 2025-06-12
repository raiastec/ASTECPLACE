from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.ImageField(upload_to='icones/categorias/', blank=True, null=True)
    

    def __str__(self):
        return self.nome

# Create your models here.
