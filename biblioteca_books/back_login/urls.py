from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import livros_favoritos_view
#aqui são os caminhos/rotas, pegando das views, como o nome já demonstra, podermos visualizar tudo, meio que cria o endereço, cada endereço url está ligado a uma view
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # aqui ele gera o token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para renovar o token
    path('livros_favoritos/', views.livros_favoritos_view, name='livros_favoritos'), # aqui estão os livros favoritos do usuario
]
