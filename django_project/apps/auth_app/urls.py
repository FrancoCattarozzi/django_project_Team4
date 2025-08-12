from django.urls import path
from django.contrib.auth import views as auth_views
from .views import exit, RegisterView

urlpatterns = [
    path('logout/', exit, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]