from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('edit/<str:pk>', views.edit_product, name='edit_product'),
    path('delete/<str:pk>', views.delete_product, name='delete_product'),
    path('details/<str:pk>', views.product_details, name='product_details'),
]