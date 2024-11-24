from django.contrib.auth.backends import BaseBackend
from .models import User

class EmailBackend(BaseBackend):
    """
    Backend personalizado para autenticar usuários com base no email_us.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Verifica se o usuário existe pelo email
            user = User.objects.get(email_us=email)
            
            # Valida se a senha fornecida corresponde à senha do banco
            if user.password_user == password:  # Substitua por hash se necessário
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, id_user):
        """
        Retorna o usuário com base no ID, ou None se ele não existir.
        """
        try:
            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None
