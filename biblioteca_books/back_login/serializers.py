from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class LoginSerializer(serializers.Serializer):
    email_us = serializers.EmailField()
    password_user = serializers.CharField(write_only=True)

    def validate(self, data):
        email_us = data.get('email_us')
        password_user = data.get('password_user')

        # Usar o backend de autenticação para verificar se o usuário existe
        user = authenticate(request=self.context.get('request'), email=email_us, password=password_user)

        if not user:
            raise serializers.ValidationError("Usuário ou senha incorretos")

        # Gerar o token JWT para o usuário
        refresh = RefreshToken.for_user(user)

        # Obter os livros favoritos do usuário
        livros_favoritos = self.get_user_books(user)

        # Retorna os dados do login e os livros favoritos
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'livros_favoritos': livros_favoritos,
        }

    def get_user_books(self, user):
        # Pega os livros favoritos do usuário
        livros_favoritos = user.livros_favoritos.all()
        return [
            {
                'id_livro': books.id_livro,
                'nome_livro': books.nome_livro,
                'nome_autor': books.nome_autor,
            }
            for books in livros_favoritos
        ]