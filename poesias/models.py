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
    
class Poesia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=1000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__ (self):
        return self.titulo

class Venda(models.Model):
    metodo_pagamento = models.CharField(max_length=100, default ='PIX')
    data_venda = models.DateField(auto_now=True)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    poesia = models.ForeignKey(Poesia, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.metodo_pagamento