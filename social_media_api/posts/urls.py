from django.urls import path
from .views import PostListCreateAPIView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create')
        
]
