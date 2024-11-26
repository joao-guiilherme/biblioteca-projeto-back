import os
import django
import sys

sys.path.append(r'C:\Users\Rose\desktop\biblioteca-projeto-back\biblioteca_books')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_books.settings')

django.setup()
#esse aqui serve pra o banco entender que quando o usuario der post da senha, que está normal, ele ler o hash do banco
from back_login.models import User  # utilizando o modelo de user do banco
# Buscar todos os usuários
users = User.objects.all()

# aqui ele pega a senha que foi colocada no post e converte para hash, para que tenha uma leitura correta 
# no banco, já que lá está armazenada como hash e não como senha normal
for user in users:
    user.set_password(user.password)  # Gera o hash da senha
    user.save()  # Salva o usuário com a senha hashada
