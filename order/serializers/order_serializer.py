from rest_framework import serializers

<<<<<<< HEAD
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerialzier(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
=======
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
<<<<<<< HEAD
    class Meta:
        model = Productfields = ['product', 'total']
=======

    class Meta:
        model = Order
        fields = ["product", "total", "user", "products_id"]
        extra_kwargs = {"product": {"required": False}}

    def create(self, validated_data):
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

        return order
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
