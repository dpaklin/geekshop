from django.urls import path
from adminapp.views import (
    # products,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    ProductsListView,
    ProductDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView,
    ProductCategoryListView, ProductCategoryCreateView, ProductCategoryUpdateView, ProductCategoryDeleteView,
)

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', ProductCategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', ProductsCreateView.as_view(), name='product_create'),
    # path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/category/<int:pk>/', ProductsListView.as_view(), name='products'),
    path('products/read/<int:pk>/', ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='product_delete'),
]