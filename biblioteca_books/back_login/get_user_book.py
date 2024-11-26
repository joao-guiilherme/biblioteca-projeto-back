


from back_login.models import User, Books
#esse aqui é uma orm, para retornar dados do banco
# Obtém todos os livros favoritos de um usuário
user = User.objects.get(user_id=1)  # aqui ele busca através do id, nesse exemplo, o id é 1

# Acesse os livros favoritos do usuário
livros_favoritos = user.user_user_livros_favoritos.all()

# Agora você pode acessar o id_user e id_books
for books in livros_favoritos:
    print(f"User ID: {user.id_user}, Book ID: {livros_favoritos.id_books}")
