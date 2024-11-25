import os
import django
import sys

# Altere o caminho para o diretório correto onde 'biblioteca_books' está localizado
sys.path.append(r'C:\Users\Rose\desktop\biblioteca-projeto-back\biblioteca_books')

# Defina o módulo de configurações
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_books.settings')


django.setup()


from back_login.models import User 
from django.contrib.auth.models import User


users = User.objects.all()

for user in users:
    user.set_password(user.password_user) 
    user.save()  
