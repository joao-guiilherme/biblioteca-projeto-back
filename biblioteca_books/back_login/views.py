from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from .models import Books

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email_us')
        password = request.data.get('password_user')

        # autentica o usuário
        user = authenticate(request=request, username=email, password=password)

        if user is None:
            return Response({'detail': 'Usuário ou senha incorretos'}, status=status.HTTP_400_BAD_REQUEST)

        # gera tokens JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # pega os livros favoritos
        livros_favoritos = self.get_user_books(user)
        
        return Response({
            'access': access_token,
            'refresh': str(refresh),
            'livros_favoritos': livros_favoritos
        }, status=status.HTTP_200_OK)

    def get_user_books(self, user):
        # pega os livros favoritos do usuario
        livros_favoritos = user.livros_favoritos.all()
        return [
            {
                'id_books': book.id_books,
                'nome_livro': book.nome_livro,
                'nome_autor': book.nome_autor,
            }
            for book in livros_favoritos
        ]


def login_view(request):
    return render(request, 'login.html')


from django.shortcuts import render

def livros_view(request):
    return render(request, 'livros.html')
