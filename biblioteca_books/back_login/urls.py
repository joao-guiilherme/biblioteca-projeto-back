from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obter o token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para renovar o token
    path('livros-favoritos/', views.livros_favoritos_view, name='livros-favoritos'),
]
