from django.urls import path
from .views import home_view, detalhe_produto  # importe também a view detalhe_produto
from anuncios import views  # pode manter se quiser usar views.busca_anuncios etc

urlpatterns = [
    path('', home_view, name='home'),
    path('busca/', views.busca_anuncios, name='busca_anuncios'),
    path('categorias/<int:categoria_id>/', views.anuncios_por_categorias, name='anuncios_por_categorias'),
    path('formulario/', views.formulario_anunciar, name='formulario_anunciar'),
    path('enviar-lead/', views.enviar_lead_bitrix, name='enviar_lead_bitrix'),
    path('produto/<int:pk>/', detalhe_produto, name='detalhe_produto'),  # use detalhe_produto direto
]
