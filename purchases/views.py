from rest_framework import viewsets
from users.permissions import IsAdminOrReadOnly
from .models import Supplier, Purchase, PurchaseDetail
from .serializers import (
    SupplierSerializer,
    PurchaseSerializer,
    PurchaseDetailSerializer
)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminOrReadOnly]

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminOrReadOnly]

class PurchaseDetailViewSet(viewsets.ModelViewSet):
    queryset = PurchaseDetail.objects.all()
    serializer_class = PurchaseDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
