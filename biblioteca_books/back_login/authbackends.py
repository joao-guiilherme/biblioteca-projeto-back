from django.contrib.auth.backends import BaseBackend
from .models import User

class EmailBackend(BaseBackend):
    def authenticate (self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email_us=email)

            if user.password_user == password:
                return user
        except User.DoesNotExist:
            return None
        
    def get_user(self, id_user):
        try:
            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None    