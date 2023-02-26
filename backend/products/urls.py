from django.urls import path
from . import views


urlpatterns = [

    path('', views.product, name='product'),

    path('<slug:slug>/', views.product_info, name='product-info'),
]

