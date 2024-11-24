from django.urls import path
from .views import LoginView
from .views import LoginView

from django.urls import path
from .views import login_view, LoginView

urlpatterns = [
    path('login/', login_view, name='login'), 
    path('api/login/', LoginView.as_view(), name='login-api')
]
