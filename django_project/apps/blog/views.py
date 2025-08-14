from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, User, Comentario

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms import modelform_factory 
from .forms import CreatePostForm, UpdatePostForm
from .models import Categoria, Comentario

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.all()
        categoria_id = self.request.GET.get('categorias', '0')
        if categoria_id != '0':
            queryset = queryset.filter(categorias__id=categoria_id).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_activa'] = int(self.request.GET.get('categorias', 0))
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ComentarioForm = modelform_factory(Comentario, fields = ['contenido'])
        context['form'] = ComentarioForm
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

# ---------------- VISTAS COMENTARIOS -----------------

class ComentarioCreateView(CreateView):
    model = Comentario
    fields = ['contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.post_id = self.kwargs['pk']

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})
    
class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'comentario_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
class ComentarioUpdateView(UpdateView):
    model = Comentario
    fields = ['contenido']
    template_name = 'comentario_update_form.html'
    success_url = reverse_lazy('post_list')

# Posteos fuera de admin

class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post_update_form.html'
    success_url = reverse_lazy('post_list')