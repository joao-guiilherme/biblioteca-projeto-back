from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Modelo de Livros
class Books(models.Model):
    id_books = models.AutoField(primary_key=True)
    nome_livro = models.CharField(max_length=255)
    nome_autor = models.CharField(max_length=255)

    class Meta:
        db_table = 'books'  # Nome da tabela de livros no banco

# Gerenciador de Usuários Personalizado
class UserManager(BaseUserManager):
    def create_user(self, email_us, password=None, **extra_fields):
        if not email_us:
            raise ValueError('O email é obrigatório')
        email_us = self.normalize_email(email_us)
        user = self.model(email_us=email_us, **extra_fields)
        user.set_password(password)  # Armazena a senha de forma segura
        user.save(using=self._db)
        return user

    def create_superuser(self, email_us, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email_us, password, **extra_fields)

# Modelo de Usuário Personalizado
class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
    email_us = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=128)

    # Relacionamento Many-to-Many com Books
    livros_favoritos = models.ManyToManyField(Books, related_name='favoritados')

    # Configuração de User
    USERNAME_FIELD = 'email_us'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    class Meta:
        db_table = 'user'  # Nome da tabela de usuários no banco
