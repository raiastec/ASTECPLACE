from django.contrib import admin
from .models import Anuncios, ImagemAnuncios
from .models import Noticia

admin.site.register(Noticia)

class ImagemAnunciosInline(admin.TabularInline):
    model = ImagemAnuncios
    extra = 3


@admin.register(Anuncios)
class AnunciosAdmin(admin.ModelAdmin):
    inlines = [ImagemAnunciosInline]

