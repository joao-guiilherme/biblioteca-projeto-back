from django.contrib.auth.backends import BaseBackend
from .models import User

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User  # Importando o modelo de usuário

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

class EmailBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Buscar o usuário pelo e-mail
            user = User.objects.get(email_us=email)
            
            # Verificar se a senha fornecida corresponde ao hash armazenado no banco de dados
            if user and check_password(password, user.password_user):  # Usando check_password
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, id_user):
        try:
            # Buscar usuário pelo ID
            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None
