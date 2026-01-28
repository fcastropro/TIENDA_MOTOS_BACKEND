from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, UserViewSet, LoginView, LogoutView, MeView

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
]
urlpatterns += router.urls
