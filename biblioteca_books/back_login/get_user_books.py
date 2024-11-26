from back_login.models import User, Books

# Obtém todos os livros favoritos de um usuário
user = User.objects.get(id_user=1)  # Substitua 1 pelo ID do usuário desejado

# Acesse os livros favoritos do usuário
livros_favoritos = user.user_user_livros_favoritos.all()

# Agora você pode acessar o id_user e id_books
for books in livros_favoritos:
    print(f"User ID: {user.id_user}, Book ID: {livros_favoritos.id_books}")
