from django.urls import path
from .views import LoginView
from .views import UserRegisterView
from .views import LoginView, UserRegisterView

from django.urls import path
from .views import login_view, LoginView, UserRegisterView

urlpatterns = [
    path('login/', login_view, name='login'), 
    path('api/login/', LoginView.as_view(), name='login-api'),  
    path('register/', UserRegisterView.as_view(), name='register'), 
    path('livros/', views.livros_view, name='livros'),
]
