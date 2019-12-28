from django.db import models
from django.utils.timezone import now

# Modelo de usuario donde estan contenidos todos los usarios de nuestro panel de administrador
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de actualizacion')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title =  models.CharField(max_length = 200, verbose_name='Titulo')
    content = models.TextField(verbose_name = 'Contenido')
    published = models.DateTimeField(verbose_name = 'Fecha de publicacion', default = now)
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'blog', null = True, blank= True)
    author = models.ForeignKey(User, verbose_name = 'Autor', on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category , verbose_name = 'Categoria', related_name="get_posts")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']

    def __str__(self):
        return self.title