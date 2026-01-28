from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet

router = DefaultRouter()
router.register(r'contacts', ContactMessageViewSet)

urlpatterns = router.urls
