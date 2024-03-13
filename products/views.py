# Views

from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# View for creating a bulk Product instance
class ProductBulkCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer