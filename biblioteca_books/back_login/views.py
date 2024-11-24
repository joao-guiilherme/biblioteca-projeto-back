from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from .models import Books

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email_us')
        password = request.data.get('password_user')

        # Tenta autenticar o usuário com o email e senha fornecidos
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Se a autenticação for bem-sucedida, faz o login do usuário
            login(request, user)
            return Response({'status': 'success', 'message': 'Login bem-sucedido!'}, status=status.HTTP_200_OK)
        else:
            # Caso contrário, envia uma mensagem de erro
            return Response({'status': 'error', 'message': 'Usuário ou senha incorretos.'}, status=status.HTTP_401_UNAUTHORIZED)

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


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['GET'])
def livros_favoritos_view(request):
    """
    View para retornar os livros favoritos do usuário autenticado.
    """
    user = request.user  # Obtém o usuário autenticado
    if not user.is_authenticated:
        return Response({'status': 'error', 'message': 'Usuário não autenticado.'}, status=401)

    # Obter os livros favoritos do usuário
    livros_favoritos = user.livros_favoritos.all()
    livros = [
        {
            'id_books': books.id_books,
            'nome_livro': books.nome_livro,
            'nome_autor': books.nome_autor,
        }
        for books in livros_favoritos
    ]
    return Response({'status': 'success', 'livros': Books}, status=200)


def login_view(request):
    return render(request, 'login.html')


from django.shortcuts import render

def livros_view(request):
    return render(request, 'livros.html')
