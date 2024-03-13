from django.db import models

# Product model definition
class Product(models.Model):
    # Field for the name of the product
    name = models.CharField(max_length=255)
    # Field for the image URL of the product
    image = models.CharField(max_length=255)

# ProductVariant model definition
class ProductVariant(models.Model):
    # Field for the stock keeping unit (SKU) of the product variant
    sku = models.CharField(max_length=255)
    # Field for the name of the product variant
    name = models.CharField(max_length=255)
    # Field for the price of the product variant, with a maximum of 10 digits and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Field for additional details or description of the product variant
    details = models.CharField(max_length=255)
    # Foreign key relationship with the Product model, specifying that each product variant belongs to a single product
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)