from django.db import models

class Books(models.Model):
    id_books = models.IntegerField(primary_key=True)
    nome_livro = models.CharField(db_column='nome_livro', max_length=45)
    nome_autor = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'books'


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    email_us = models.CharField(max_length=45)
    password_user = models.CharField(max_length=45)


    livros_favoritos = models.ManyToManyField(Books, related_name="Favoritados")

    class Meta:
        managed = True
        db_table = 'user'