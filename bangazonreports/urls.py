from bangazonreports.views.favorites_by_customer import customer_favorites_list
from django.urls import path
from .views import customer_favorites_list

urlpatterns = [
    path('reports/favoritesellers', customer_favorites_list),
]
