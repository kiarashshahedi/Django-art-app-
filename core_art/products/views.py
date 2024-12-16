from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Product
from .serializers import ProductSerializer

# Product List
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Sellers can only see their own products
        if self.request.user.is_seller:
            return Product.objects.filter(seller=self.request.user)
        raise PermissionDenied("You do not have permission to view this content.")

    def perform_create(self, serializer):
        if not self.request.user.is_seller:
            raise PermissionDenied("Only sellers can create products.")
        serializer.save(seller=self.request.user)

# Product Detail
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Sellers can only manage their own products
        if self.request.user.is_seller:
            return Product.objects.filter(seller=self.request.user)
        raise PermissionDenied("You do not have permission to view this content.")
