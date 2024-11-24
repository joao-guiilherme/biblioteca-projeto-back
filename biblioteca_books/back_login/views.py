from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from .models import Books, User

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Usar o serializer para validar os dados da requisição
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            # Se os dados forem válidos, retorna os dados do login (tokens e livros favoritos)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            # Caso contrário, retorna erros de validação
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Books

from rest_framework.permissions import IsAuthenticated

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
            'id_livro': books.id_livro,
            'nome_livro': books.nome_livro,
            'nome_autor': books.nome_autor,
        }
        for books in livros_favoritos
    ]

    return Response({'status': 'success', 'livros': livros}, status=200)
