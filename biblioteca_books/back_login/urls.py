from django.urls import path
from . import views
from .views import LoginView, livros_favoritos_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-api'),
        path('livros_favoritos/', views.livros_favoritos_view, name='livros_favoritos'),
]
