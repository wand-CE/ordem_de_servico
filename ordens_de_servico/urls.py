from django.urls import path

from ordens_de_servico import views

urlpatterns = [
    path('cadastro', views.CadastrarOrdem.as_view(), name='cadastrar_ordem'),
    path('listar', views.ListarOrdens.as_view(), name='listar_ordens'),
    path('editar/<int:pk>/', views.EditarOrdem.as_view(), name='editar_ordem'),
    path('excluir/<int:pk>/', views.ExcluirOrdem.as_view(), name='excluir_ordem'),
]
