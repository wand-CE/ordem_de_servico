from django.urls import path

from servicos import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LogarFuncionario.as_view(), name='login'),
    path('logout/', views.DeslogarFuncionarioView.as_view(), name='deslogar'),

    path('clientes/cadastro', views.CadastroClienteView.as_view(), name='cadastrar_cliente'),
    path('clientes/listar', views.ListarClienteView.as_view(), name='listar_clientes'),
    path('clientes/editar/<int:pk>/', views.EditarClienteView.as_view(), name='editar_cliente'),
    path('clientes/excluir/<int:pk>/', views.ExcluirClienteView.as_view(), name='excluir_cliente'),

    path('marca/cadastro', views.CadastrarMarca.as_view(), name='cadastrar_marca'),

    path('produtos/cadastro', views.CadastrarProduto.as_view(), name='cadastrar_produto'),
    path('produtos/listar', views.ListarProdutoView.as_view(), name='listar_produtos'),
    path('produtos/editar/<int:pk>/', views.EditarProduto.as_view(), name='editar_produto'),
    path('produtos/excluir/<int:pk>/', views.ExcluirProduto.as_view(), name='excluir_produto'),

    path('ordem-servico/cadastro', views.CadastrarOrdem.as_view(), name='cadastrar_ordem'),
    path('ordem-servico/listar', views.ListarOrdens.as_view(), name='listar_ordens'),
    path('ordem-servico/editar/<int:pk>/', views.EditarOrdem.as_view(), name='editar_ordem'),
    path('ordem-servico/excluir/<int:pk>/', views.ExcluirOrdem.as_view(), name='excluir_ordem'),
]
