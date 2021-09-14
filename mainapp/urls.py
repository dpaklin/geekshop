from django.urls import path, re_path
from .views import products, product, products_ajax
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(products_ajax)),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('product/<int:pk>/', product, name='product'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(products_ajax)),
]
