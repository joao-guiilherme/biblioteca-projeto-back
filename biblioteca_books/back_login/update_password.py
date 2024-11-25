import os
import django
import sys

sys.path.append(r'C:\Users\Rose\desktop\biblioteca-projeto-back\biblioteca_books')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_books.settings')

django.setup()

from back_login.models import User  # Certifique-se de usar o modelo de User personalizado

# Buscar todos os usuários
users = User.objects.all()

# Atualizar a senha para hash
for user in users:
    user.set_password(user.password)  # Gera o hash da senha
    user.save()  # Salva o usuário com a senha hashada
