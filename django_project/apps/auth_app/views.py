from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

# username / email y pasword

def exit(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
