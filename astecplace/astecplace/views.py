from django.shortcuts import render


def home_views(request):
    anuncios = anuncios.objects.all()
    return render(request, 'home/home.html', {'anuncios': anuncios})