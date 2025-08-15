from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control m-1'}),
        label='Usuario',
        help_text=''
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control  m-1'})
    )
    first_name = forms.CharField(
        label="Nombre",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control  m-1'})
    )
    last_name = forms.CharField(
        label="Apellido",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control  m-1'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control  m-1'}),
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control  m-1'}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user