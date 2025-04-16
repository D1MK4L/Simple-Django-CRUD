from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import TextPost
from .serializers import UserSerializer, TokenSerializer, TextPostSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import status
from django.contrib.auth import authenticate

# User Registration View
class UserRegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,  # Define the expected input serializer
        responses={201: openapi.Response("User created successfully")}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({
                'user': {
                    'username': user.username,
                    'email': user.email,
                },
                'tokens': tokens
            })
        return Response(serializer.errors, status=400)

# Text Post ViewSet
class TextPostViewSet(viewsets.ModelViewSet):
    queryset = TextPost.objects.all()
    serializer_class = TextPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['delete'])
    def delete_post(self, request, pk=None):
        post = self.get_object()
        if post.user == request.user:
            post.delete()
            return Response(status=204)
        return Response({"detail": "Permission denied"}, status=403)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return TextPost.objects.filter(user=user)  # Only fetch posts from the logged-in user
        return TextPost.objects.none()  # Return empty queryset for non-authenticated users

# Login with JWT
class TokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        from rest_framework_simplejwt.tokens import RefreshToken
        from rest_framework_simplejwt.views import TokenObtainPairView
        return TokenObtainPairView.as_view()(request, *args, **kwargs)
    
# Custom Token Obtain View to use username for authentication
class CustomTokenObtainPairView(APIView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        request_body=CustomTokenObtainPairSerializer,  # The request body should be the serializer used
        responses={200: openapi.Response('Token issued successfully')}
    )
    def post(self, request, *args, **kwargs):
        # Get email and password from request data
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user using email instead of username
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Generate token pair (access and refresh)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
