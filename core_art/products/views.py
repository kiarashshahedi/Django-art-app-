from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product, ProductImage, Category, Tag
from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer, TagSerializer

# Product List
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()

    # Add filters
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Define filter fields
    filterset_fields = ['category', 'tags', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']


    
    # def get_queryset(self):
    #     # Sellers can only see their own products
    #     if self.request.user.is_seller:
    #         return Product.objects.filter(seller=self.request.user)
    #     # buyer see
    #     elif self.request.user.is_buyer:
    #         return Product.objects.all()
    #     raise PermissionDenied("You do not have permission to view this content.")

    # def perform_create(self, serializer):
    #     if not self.request.user.is_seller:
    #         raise PermissionDenied("Only sellers can create products.")
    #     serializer.save(seller=self.request.user)

# Product Detail
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Sellers can only manage their own products
        if self.request.user.is_seller:
            return Product.objects.filter(seller=self.request.user)
        # buyer see
        elif self.request.user.is_buyer:
            return Product.objects.all()
        raise PermissionDenied("You do not have permission to view this content.")
    
# Category list view
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Tag LIst View
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer