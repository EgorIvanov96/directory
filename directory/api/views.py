import openpyxl
from djoser.views import UserViewSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User
from reviews.models import Categories, Materials
from .serializers import (UserSerializer, CategoriesSerializer,
                          MaterialsSerializer, TreeCategorySerializer)


class UserViewSet(UserViewSet):
    """Вьюсет для пользователей и авторов."""

    quryset = User.objects.all()
    serializer_class = UserSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Вьюсет для категерий."""

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def list(self, request):
        categories = Categories.objects.values_list('name_categories',
                                                    'category_code')
        categories_list = list(categories)
        return Response(categories_list)


class TreeCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для дерева категерий."""

    queryset = Categories.objects.prefetch_related('materials_set')
    serializer_class = TreeCategorySerializer


class MaterialsViewSet(viewsets.ModelViewSet):
    """Вьюсет для материалов."""

    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer

    @action(detail=False, methods=['post'], url_path='upload')
    def post(self, request):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.xlsx'):
            return Response(
                {'Неверный формат файла.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name_materials = row[0]
            name_categories = row[1]
            materials_code = row[2]
            price = row[3]

            try:
                category = Categories.objects.get(
                    name_categories=name_categories)
                data = {
                    'name_materials': name_materials,
                    'categories_materials': category.id,
                    'materials_code': materials_code,
                    'price': price
                }

                serializer = MaterialsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)

            except Categories.DoesNotExist:
                return Response(
                    {'Ошибка': f'Категория {name_categories} не найдена.'},
                    status=status.HTTP_400_BAD_REQUEST)

        return Response({'Данные успешно добавлены'},
                        status=status.HTTP_201_CREATED)
