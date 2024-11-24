from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class LoginSerializer(serializers.Serializer):
    email_us = serializers.EmailField()
    password_user = serializers.CharField(write_only=True)

    def validate(self, data):
        # Tenta autenticar o usuário
        email_us = data.get('email_us')
        password_user = data.get('password_user')

        user = authenticate(request=self.context.get('request'), email_us=email_us, password=password_user)

        if not user:
            raise serializers.ValidationError("Usuário ou senha incorretos")

        # Cria os tokens JWT
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'livros_favoritos': self.get_user_books(user),
        }

    def get_user_books(self, user):
        """
        Retorna os livros favoritos do usuário.
        """
        livros_favoritos = user.livros_favoritos.all()
        return [
            {
                'nome_livro': books.nome_livro,
                'nome_autor': books.nome_autor,
            }
            for books in livros_favoritos
        ]