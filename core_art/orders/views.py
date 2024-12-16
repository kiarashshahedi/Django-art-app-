from rest_framework import generics, permissions
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe

# View Cart details
class CartView(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure each user has a single cart
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

# Order and Buy
class CheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        total_price = 0
        admin_commission = 0.1  # 10% admin commission
        orders = []

        for item in cart.items.all():
            total_price += item.get_total_price()
            commission = item.get_total_price() * admin_commission
            seller_earnings = item.get_total_price() - commission
            orders.append(Order(
                buyer=self.request.user,
                seller=item.product.seller,
                product=item.product,
                quantity=item.quantity,
                total_price=item.get_total_price(),
                admin_commission=commission,
                seller_earnings=seller_earnings
            ))

        Order.objects.bulk_create(orders)
        cart.items.all().delete()

# Payment
class PaymentView(APIView):
    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            amount = sum(item.get_total_price() for item in cart.items.all()) * 100  # Amount in cents

            # Create Stripe payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='usd',
                metadata={'user_id': request.user.id},
            )
            return Response({'client_secret': intent['client_secret']}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)