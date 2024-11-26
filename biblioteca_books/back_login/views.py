from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, BookSerializer
from .models import Books, User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
import logging

#esse aqui é a view do login, que utiliza o serializer de login(os dados do modelo user)
# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        logger.info("Iniciando processo de login.")
        
        # Usar o serializer para validar os dados da requisição
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            logger.info(f"Login bem-sucedido para o usuário: {serializer.validated_data.get('email', 'email desconhecido')}")
            # Se os dados forem válidos, retorna os dados do login (tokens)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Falha no login. Erros de validação: {serializer.errors}")
            # Caso contrário, retorna erros de validação
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

# View de Livros Favoritos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def livros_favoritos_view(request):
    logger.info("Iniciando visualização de livros favoritos.")
    
    user = request.user  # Obtém o usuário autenticado
    logger.info(f"Usuário autenticado: {user.email_us} (ID: {user.id_user})")
    
    try:
        # Acessa os livros favoritos através do relacionamento muitos para muitos
        favoritos = user.livros_favoritos.all()
        logger.info(f"{favoritos.count()} livros favoritos encontrados para o usuário.")
        
        livros = [
            {
                'id_books': livro.id_books,
                'nome_livro': livro.nome_livro,
                'nome_autor': livro.nome_autor,
            }
            for livro in favoritos
        ]
        logger.info("Lista de livros favoritos construída com sucesso.")
        
        return Response({'status': 'success', 'livros': livros}, status=200)
    
    except Exception as e:
        logger.error(f"Erro ao obter livros favoritos: {str(e)}")
        return Response({'status': 'error', 'message': 'Erro ao acessar livros favoritos.'}, status=500)
