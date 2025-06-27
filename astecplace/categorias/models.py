from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
  
    icone = models.ImageField(upload_to='icones/categorias/', blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de exibição")


    def __str__(self):
        return self.nome



    class Meta:
        ordering = ['ordem']



      

# Create your models here.
