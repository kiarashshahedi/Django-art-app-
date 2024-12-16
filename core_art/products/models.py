# from django.db import models
# from users.models import User

# class Product(models.Model):
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     categories = models.ManyToManyField(Category)
#     images = models.ManyToManyField(ProductImage)
#     date_added = models.DateTimeField(auto_now_add=True)
