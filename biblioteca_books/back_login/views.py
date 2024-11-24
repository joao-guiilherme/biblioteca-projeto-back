from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from .models import Books, User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes




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
        
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Garantir que o usuário está autenticado
def livros_favoritos_view(request):
    user = request.user  # Obtém o usuário autenticado
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
