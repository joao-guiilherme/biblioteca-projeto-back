from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Books
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    email_us = serializers.EmailField()
    password_user = serializers.CharField(write_only=True)

    def validate(self, data):
        email_us = data.get('email_us')
        password_user = data.get('password_user')

        # vai autenticar usando email e senha
        user = authenticate(request=self.context.get('request'), username=email_us, password=password_user)
        if user is None:
            raise serializers.ValidationError("Usuário ou senha incorretos")
        
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'livros_favoritos': self.get_user_books(user)
        }
    
    def get_user_books(self, user):
       
        livros_favoritos = user.livros_favoritos.all()
        return [
            {
                'id_books': livro.id_books,  
                'nome_livro': livro.nome_livro,
                'nome_autor': livro.nome_autor,
            }
            for livro in livros_favoritos]

# registra usuarios
class UserRegisterSerializer(serializers.ModelSerializer):
    password_user = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email_us', 'password_user', 'username']

    def create(self, validated_data):
        password_user = validated_data.pop('password_user')
        user = User(**validated_data)
        user.set_password(password_user)  # criptografa a senha
        user.save()
        return user