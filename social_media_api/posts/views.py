import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse
from . import views
def my_view(request):
    return HttpResponse("Hello, world!")
 
class CustomLoginView(APIView):
    """Custom login view to handle login with username and password"""
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    """View to register a new user"""
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class ProtectedPostView(APIView):
    """View for authenticated users to access protected posts"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})


class PostListCreateAPIView(APIView):
    """View to list and create posts"""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(AuthLoginView):
    """Using Django's built-in LoginView to render login template"""
    #template_name = 'login.html'  # Optional, define if you're rendering a template for login
