from .models import Post
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['autor']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple,
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'receta': forms.Textarea(attrs={'class': 'form-control'}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categorias']
        widgets = {
            'categorias': forms.CheckboxSelectMultiple,
        }