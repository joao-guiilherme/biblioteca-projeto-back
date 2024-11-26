from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Books

#o serializer serve pra meio que converter os modelos em classes, para poder ser utilado no post

class LoginSerializer(serializers.Serializer):
    #esse é o serializer que converte os dados de email_us e password em dados para login, utiliza os campos email_us e password
    email_us = serializers.EmailField()
    password = serializers.CharField(write_only=True)

#aqui ele valida
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

#esse aqui utiliza a tabela user_livros_favoritos, que é onde estão os livros favoritos do usuario armazenados no banco
    def get_user_books(self, user):
        # Pega os livros favoritos do usuário
        livros_favoritos = livros_favoritos.all()

        # Usando o BookSerializer para retornar os livros favoritos com formato adequado
        return BookSerializer(livros_favoritos, many=True).data

#esse tem a mesma logica do loginserializer, só que está convertendo os dados do modelo books
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id_books', 'nome_livro', 'nome_autor']
