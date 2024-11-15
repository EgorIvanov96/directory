from rest_framework import serializers

from users.models import User
from reviews.models import Categories, Materials


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username ')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения категорий."""

    class Meta:
        model = Categories
        fields = ('name_categories', 'category_code')


class MaterialsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения материалов."""

    class Meta:
        model = Materials
        fields = ('name_materials', 'categories_materials',
                  'materials_code', 'price')


class TreeCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения дерева категорий."""

    materials = MaterialsSerializers(
        source='materials_set',
        many=True,
        read_only=True
    )
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields = ('name_categories', 'category_code',
                  'materials', 'total_price')

    def get_total_price(self, obj):
        """Подсчет общей суммы всех материалов в категории."""

        materials = obj.materials_set.all()
        return sum(material.price for material in materials)
