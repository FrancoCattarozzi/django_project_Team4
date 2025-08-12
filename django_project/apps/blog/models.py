from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120, null=False, blank=False, verbose_name='Título')
    contenido = models.TextField(verbose_name='Contenido')
    receta = models.TextField(verbose_name='Receta', null=True, blank=True)
    instrucciones = models.TextField(verbose_name='Instrucciones', null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media/posts')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-fecha_creacion"]

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.username}'
    
    class Meta:
        db_table = 'comentarios'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha_creacion']