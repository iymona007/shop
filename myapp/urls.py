from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('blog-details/', blog_details, name='blog_details'),
    path('blog/', blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('main.html/', main, name='main'),
    path('product-details/', product_details, name='product_details'),
    path('shop-cart/', shop_cart, name='shop_cart'),
    path('shop/', shop, name='shop'),
]

