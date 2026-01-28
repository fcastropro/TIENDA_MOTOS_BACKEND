from rest_framework import viewsets
from users.permissions import IsAdminOrReadOnly
from .models import Inventory
from .serializers import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAdminOrReadOnly]
