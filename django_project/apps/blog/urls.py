from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView, ComentarioCreateView, PostCreateView, PostUpdateView, ComentarioDeleteView, ComentarioUpdateView, like_post
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comentar/', ComentarioCreateView.as_view(), name='comentar_post'),
    path('comentario/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario_delete'),
    path('comentario/<int:pk>/update/', ComentarioUpdateView.as_view(), name='comentario_update'),
    path('like/<int:pk>/', like_post, name='like_post'),
]