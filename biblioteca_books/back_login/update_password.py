import os
import django

# Defina o caminho correto para o arquivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_books.settings')

# Inicializa o Django
django.setup()

# Agora, você pode importar as models
from back_login.models import User  # Importando as models corretamente
from django.contrib.auth.models import User

# Obtém todos os usuários com senhas em texto simples
users = User.objects.all()

for user in users:
    user.set_password(user.password_user)  # Converte para senha hashada
    user.save()  # Salva o usuário com a senha hashada
