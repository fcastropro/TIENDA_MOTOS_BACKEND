from rest_framework import viewsets
from users.permissions import IsAdminOrReadOnly
from .models import PaymentMethod, Invoice, InvoiceDetail
from .serializers import PaymentMethodSerializer, InvoiceSerializer, InvoiceDetailSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAdminOrReadOnly]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAdminOrReadOnly]

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
