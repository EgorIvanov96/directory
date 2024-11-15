from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CategoriesViewSet, MaterialsViewSet, TreeCategoryViewSet


app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('materials', MaterialsViewSet, basename='materials')
router.register('treecategory', TreeCategoryViewSet, basename='treecategory')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
