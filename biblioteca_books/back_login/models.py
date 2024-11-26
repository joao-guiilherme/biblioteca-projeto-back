from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Books(models.Model):
    id_books = models.AutoField(primary_key=True)  
    nome_livro = models.CharField(db_column='nome_livro', max_length=45)
    nome_autor = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'books'




# Gerenciador de usuários personalizado
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


class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)  # AutoField é o tipo recomendado para chave primária
    email_us = models.EmailField(unique=True)  # Tornar o email único
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=128)  # A senha deve ser longa o suficiente para armazenar senhas hasheadas

    user_livros_favoritos = models.ManyToManyField(Books, related_name="Favoritados")

    # Configurações do modelo de usuário
    USERNAME_FIELD = 'email_us'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # Usar o gerenciador de usuários personalizado

    class Meta:
        managed = True
        db_table = 'user'