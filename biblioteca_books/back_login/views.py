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
@permission_classes([IsAuthenticated])
def livros_favoritos_view(request):
    user = request.user  # Obtém o usuário autenticado
    livros_favoritos = user.user_livros_favoritos.all()  # Acessa os livros favoritos através do relacionamento many-to-many
    livros = [
        {
            'id_books': livro.id_books,
            'nome_livro': livro.nome_livro,
            'nome_autor': livro.nome_autor,
        }
        for livro in livros_favoritos  # Itera sobre os livros favoritados
    ]
    return Response({'status': 'success', 'livros': livros}, status=200)

