from .models import Post, Comentario, Rating
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'receta', 'instrucciones', 'imagen', 'categorias']
        exclude = ['autor']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'receta': forms.Textarea(attrs={'class': 'form-control'}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'receta', 'instrucciones', 'imagen', 'categorias']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'receta': forms.Textarea(attrs={'class': 'form-control'}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribí tu comentario...',
                'rows': 3
            })
        }
