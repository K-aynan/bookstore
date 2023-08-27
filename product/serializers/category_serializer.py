from rest_framework import serializers
from product.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
<<<<<<< HEAD
        ]
=======
        ]
        extra_kwargs = {"slug": {"required": False}}
>>>>>>> 1e4bc09f8054df132a7460d0f0fd37450506453a
