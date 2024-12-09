from django.urls import path
from .views import PostListCreateAPIView
from django.urls import path, include

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('api/', include('posts.urls')),
]
