from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User 

class EmailBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
          
            user = User.objects.get(email_us=email)
            
            
            if user and check_password(password, user.password_user):  
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, id_user):
        try:

            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None
