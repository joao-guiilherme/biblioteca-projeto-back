from django.urls import path
from . import views
from .views import LoginView, livros_favoritos_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Mantendo a simplicidade
    path('livros-favoritos/', livros_favoritos_view, name='livros-favoritos'),  # Alterando para um formato mais legível
]
