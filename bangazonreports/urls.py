from django.urls import path
from .views import customer_favorites_list, products_over_1000, products_under_1000, completed_orders_list

urlpatterns = [
    path('reports/favoritesellers', customer_favorites_list),
    path('reports/expensiveproducts', products_over_1000),
    path('reports/inexpensiveproducts', products_under_1000),
    path('reports/completedorders', completed_orders_list)
]
