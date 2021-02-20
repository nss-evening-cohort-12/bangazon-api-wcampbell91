from bangazonreports.views.favorites_by_customer import customer_favorites_list
from django.urls import path
from .views import customer_favorites_list, products_over_1000, products_under_1000

urlpatterns = [
    path('reports/favoritesellers', customer_favorites_list),
    path('reports/expensiveproducts', products_over_1000),
    path('reports/inexpensiveproducts', products_under_1000)
]
