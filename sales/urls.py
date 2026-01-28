from rest_framework.routers import DefaultRouter
from .views import PaymentMethodViewSet, InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-details', InvoiceDetailViewSet)

urlpatterns = router.urls
