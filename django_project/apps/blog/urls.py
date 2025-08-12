from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView, ComentarioCreateView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comentar/', ComentarioCreateView.as_view(), name='comentar_post'),
]