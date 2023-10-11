
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.productListView.as_view(), name="product-list")
]