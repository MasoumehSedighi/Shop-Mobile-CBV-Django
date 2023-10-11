from django.shortcuts import render
from django.views.generic import ListView
from .import models

# Create your views here.

class productListView(ListView):
    queryset = models.Product.objects.filter(is_available=True)
    context_object_name = "products"
    template_name = "products/product_list.html"


