from django.urls import path
from . import views


urlpatterns = [

    path('', views.product, name='product'),

    path('<slug:product_slug>/', views.product_info, name='product-info'),

    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]

