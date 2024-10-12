from django.urls import path

from funcionarios import views

urlpatterns = [
    path('login/', views.LogarFuncionario.as_view(), name='login'),
    path('logout/', views.DeslogarFuncionarioView.as_view(), name='deslogar'),
]
