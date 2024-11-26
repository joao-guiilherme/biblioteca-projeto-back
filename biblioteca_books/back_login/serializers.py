from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Books
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email_us = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email_us = data.get('email_us')
        password = data.get('password')

        # Utilizando a autenticação personalizada
        user = authenticate(request=self.context.get('request'), email=email_us, password=password)

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


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id_books', 'nome_livro', 'nome_autor']


    def get_user_books(self, user):
        # Pega os livros favoritos do usuário
        livros_favoritos = user.livros_favoritos.all()
        # Retorne os livros favoritos com um formato mais adequado
        return BookSerializer(livros_favoritos, many=True).data  # Usando um serializer
