from django.urls import path

from base_app import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
