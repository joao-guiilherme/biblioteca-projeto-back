# isso aqui sou eu fazendo um teste 


from back_login.models import User, Books

# Este código faz uso de ORM do Django, ou seja, ele utiliza a abstração do banco de dados para trabalhar com os modelos definidos em models.py.
# Obtém um usuário pelo ID
user = User.objects.get(id_user=1)  # Aqui, o código busca o usuário com id_user = 1
# O relacionamento muitos para muitos é acessado através do modelo intermediário 
livros_favoritos = user.livros_favoritos.all() 
# acessar os livros favoritos do usuário
for livro in livros_favoritos:
    # Para cada livro, imprimimos o ID do usuário e o ID do livro
    print(f"User ID: {user.id_user}, Book ID: {livro.id_books}")  # Aqui é necessário usar 'livro.id_books' 
