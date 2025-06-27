from django.shortcuts import render, get_object_or_404
from .models import Anuncios
from categorias.models import Categoria
from django.db.models import Q
from .models import Noticia  # Importe Noticia
from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    anuncios = Anuncios.objects.filter(ativo=True).order_by('-criado_em')
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.order_by('-data_publicacao')[:3]
    #print("Anúncios carregados:", anuncios)
    #print("Categorias carregadas:", categorias)
    #print("Notícias carregadas:", noticias)

    return render(request, 'home/home.html', {
        'anuncios': anuncios,
        'categorias': categorias,
        'noticias': noticias,
    })
##metodo para listar os anúncios ativos
def detalhe_produto(request, pk):
    produto = get_object_or_404(Anuncios, pk=pk)
    return render(request, 'anuncios/produto_detalhe.html', {'produto': produto})


def formulario_anunciar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')

        # Aqui você pode salvar no banco, enviar email ou integrar com Bitrix24
        messages.success(request, 'Sua solicitação foi enviada com sucesso!')
        return redirect('formulario_anunciar')

    return render(request, 'formulario/formulario_anunciar')

def busca_anuncios(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        resultados = Anuncios.objects.filter(
            Q(titulo__icontains=query) |
            Q(descricao__icontains=query) |
            Q(localizacao__icontains=query)
        ).filter(ativo=True
        )

    return render(request, 'busca/busca_resultado.html', {
    'query': query,
    'resultados': resultados,
    
    })
    



def anuncios_por_categorias(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    anuncios = Anuncios.objects.filter(categoria=categoria, ativo=True)


    return render(request, 'home/home.html', {
        'categoria': categoria,
        'anuncios': anuncios,
    })

import requests
from django.shortcuts import redirect
from django.contrib import messages

def enviar_lead_bitrix(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        titulo = request.POST.get('titulo')

        url = "https://astecassessoriaagropecuaria.bitrix24.com.br/rest/31/xxnbvv4is9jfat4j/crm.lead.add.json"
        payload = {
            "FIELDS": {
                "TITLE": f"Interesse no anúncio: {titulo}",
                "NAME": nome,
                "EMAIL": [{"VALUE": email, "VALUE_TYPE": "WORK"}],
                "PHONE": [{"VALUE": telefone, "VALUE_TYPE": "WORK"}],
            }
        }

        try:
            requests.post(url, json=payload)
            messages.success(request, "Seu interesse foi enviado com sucesso para a equipe!")
        except Exception:
            messages.error(request, "Ocorreu um erro ao enviar. Tente novamente.")

    return redirect('home')
