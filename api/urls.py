from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, TextPostViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  # Correct import for JWTAuthentication
from rest_framework import permissions

# Set up the API schema
schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test API for creating and managing posts",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],  # Make the API accessible only to authenticated users
)

router = DefaultRouter()
router.register(r'posts', TextPostViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
   #  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
