from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Role, User
from .serializers import RoleSerializer, UserSerializer
from .permissions import IsAdminRole

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminRole]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminRole]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'detail': 'Email y contraseña son obligatorios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)
        if not user:
            user = User.objects.filter(email__iexact=email).first()
            if not user or not user.check_password(password):
                return Response(
                    {'detail': 'Credenciales inválidas.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        if not user.is_active:
            return Response(
                {'detail': 'Usuario inactivo.'},
                status=status.HTTP_403_FORBIDDEN
            )

        login(request, user)
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Sesión cerrada.'}, status=status.HTTP_200_OK)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UserSerializer(request.user).data
        return Response(data, status=status.HTTP_200_OK)
