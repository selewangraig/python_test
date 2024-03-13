from rest_framework import serializers
from .models import Product, ProductVariant

# Serializer for ProductVariant model
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        # Specifies the fields to be included in the serialized representation of ProductVariant
        fields = ['sku', 'name', 'price', 'details']

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    # Serializer field to represent the related ProductVariant instances
    variants = ProductVariantSerializer(many=True)
    
    class Meta:
        model = Product
        # Specifies the fields to be included in the serialized representation of Product
        fields = ['id', 'name', 'image', 'variants']

    # method to handle creation of Product instances along with associated ProductVariant instances
    def create(self, validated_data):
        # indicate the start of product creation process (just for debugging purposes)
        print("Creating product variants...")

        # Extract variants data from validated_data
        variants_data = validated_data.pop('variants', None)
        # Print variants data (just for debugging purposes)
        print("Variants data: ", variants_data)

        # Create the Product instance using remaining validated_data
        product = Product.objects.create(**validated_data)

        # If variants data is provided, create associated ProductVariant instances
        if variants_data:
            for variant_data in variants_data:
                # indicate the creation of each variant (just for debugging purposes)
                print("Creating variant: ", variant_data)
                # Create ProductVariant instance associated with the current product
                ProductVariant.objects.create(product=product, **variant_data)

        # indicate successful creation of product (just for debugging purposes)
        print("Product creation successful: ", product)
        
        return product