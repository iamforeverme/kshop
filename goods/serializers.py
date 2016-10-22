from rest_framework import serializers
from models import Producer, Brand, Product

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ('producer_name', 'produced_country')

class BrandSerializer(serializers.ModelSerializer):
    # This is for nested serializer
    producer = ProducerSerializer()
    class Meta:
        model = Brand
        fields = ('producer', 'brand_name')
        # This is for nested serializer
        depth = 2

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = ('brand', 'product_name','product_description', 'price' , 'general_photo')
        depth = 3
