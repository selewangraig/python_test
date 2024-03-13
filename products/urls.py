from django.urls import path
from .views import ProductBulkCreateView

urlpatterns = [
    path('bulk-create/', ProductBulkCreateView.as_view(), name='product_bulk_create'),
]