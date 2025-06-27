from django.shortcuts import render
from anuncios.models import Anuncios
from categorias.models import Categoria


def home_view(request):
    anuncios = Anuncios.objects.filter(ativo=True).order_by('-criado_em')
    categorias = Categoria.objects.all().order_by('ordem')

    

    return render(request, 'home/home.html', {
        'anuncios': anuncios,
        'categorias': categorias
    })

# Create your views here.
