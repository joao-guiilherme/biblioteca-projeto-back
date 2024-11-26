from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User 

#Esse aqui é uma autenticação personalizada, já que eu não estou autenticando usando o padrão do django, que seria pelo username
#Estou autenticando utilizando o email

class EmailBackend(BaseBackend):
    #primeiro ele busca no banco se o email é igual ao armazenado no banco
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email_us=email)
            print(f"Usuário encontrado: {user.email_us}, ativo: {user.is_active}")
            #após verificar se o email está no banco, se ele estiver lá, ele vai checar a senha, como ela está guardada em hash,
            #que é mais seguro, ela utiliza o check_password
            if user and user.is_active and check_password(password, user.password):
                #após chegar se a senha colocada é a mesma do banco, ele retorna o usuário do banco
                return user
            #se não encontrar, ele retorna esse aviso de senha ou usuario, que no caso é o email, não encontrados
            else:
                print("Usuário ou senha incorretos ou conta desativada.")
                return None
            #se o email não existir, ele retorna esse aviso aqui
        except User.DoesNotExist:
            print("Usuário não encontrado.")
            return None

#aqui, após ele autenticar tudo e verificar se o usuario existe no banco, ele retorna o id, que é a chave primaria do usuario

    def get_user(self, id_user):
    
        try:

            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None
