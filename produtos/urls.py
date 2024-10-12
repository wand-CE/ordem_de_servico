from django.urls import path

from produtos import views

urlpatterns = [
    path('marca/cadastro', views.CadastrarMarca.as_view(), name='cadastrar_marca'),

    path('cadastro', views.CadastrarProduto.as_view(), name='cadastrar_produto'),
    path('listar', views.ListarProdutoView.as_view(), name='listar_produtos'),
    path('editar/<int:pk>/', views.EditarProduto.as_view(), name='editar_produto'),
    path('excluir/<int:pk>/', views.ExcluirProduto.as_view(), name='excluir_produto'),
]
