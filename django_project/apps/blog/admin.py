from django.contrib import admin

from .models import Post, Categoria, Comentario

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    
admin.site.register(Categoria)
admin.site.register(Comentario)