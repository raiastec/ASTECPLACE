from django.urls import path
from .views import home_view
from anuncios import views

urlpatterns = [
    path('', home_view, name='home'),
    path('busca/', views.busca_anuncios, name='busca_anuncios'),
    path('categorias/<int:categoria_id>/', views.anuncios_por_categorias, name='anuncios_por_categorias'),
    path('formulario/', views.formulario_anunciar, name='formulario_anunciar'),
]



