from .models import Post
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['autor']
        
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categoria']