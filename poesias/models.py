# Create your models here.

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    data_publicacao = models.CharField(max_length=8)
    imagem = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.titulo