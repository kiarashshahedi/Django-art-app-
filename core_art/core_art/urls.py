from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users app
    path('users/', include('users.urls')),
    # Products app
    path('products/', include('products.urls')),
    # Orders app
    path('orders/', include('orders.urls')),



]
