from django.urls import path
from .views import PessoaAPI, CalcularPesoIdealAPI

urlpatterns = [
    path('pessoas/', PessoaAPI.as_view()), 
    path('pessoas/<str:cpf>/', PessoaAPI.as_view()),  
    path('pessoas/<str:cpf>/calcular_peso_ideal/', CalcularPesoIdealAPI.as_view()), 
]
