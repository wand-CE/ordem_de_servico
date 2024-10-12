from django.urls import path

from clientes import views

urlpatterns = [
    path('cadastro', views.CadastroClienteView.as_view(), name='cadastrar_cliente'),
    path('listar', views.ListarClienteView.as_view(), name='listar_clientes'),
    path('editar/<int:pk>/', views.EditarClienteView.as_view(), name='editar_cliente'),
    path('excluir/<int:pk>/', views.ExcluirClienteView.as_view(), name='excluir_cliente'),
]
