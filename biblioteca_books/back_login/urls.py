from django.urls import path
from . import views
from .views import login_view, LoginView, livros_favoritos_view

urlpatterns = [
    path('login/', login_view, name='login'), 
    path('api/login/', LoginView.as_view(), name='login-api'),
        path('livros_favoritos/', views.livros_favoritos_view, name='livros_favoritos'),
]
