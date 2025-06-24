from django.db import models

from usuario.models import Usuario
from categorias.models import Categoria
from django.shortcuts import render, get_object_or_404


class Anuncios(models.Model):
    CATEGORIA_CHOICES = [
        ('imovel', 'Imóvel Rural'),
        ('veiculo', 'Veículo'),
        ('maquina', 'Máquina Agrícola'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    localizacao = models.CharField(max_length=150)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    destaque = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class ImagemAnuncios(models.Model):
    anuncio = models.ForeignKey(Anuncios, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='imagens/anuncios/')
    

    def __str__(self):
        return f'Imagem de {self.anuncio.titulo}'
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    

# Create your models here.
