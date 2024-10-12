from django.urls import path

from gerenciador_base_app import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
