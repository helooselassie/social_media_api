from django.urls import path
from .views import PostListCreateAPIView, RegisterView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
]
