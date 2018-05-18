from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    
    # returns all the products in the DB
    products = Product.objects.all()
    
    # renders the products.html page and in that page 
    # we have access to all the products
    return render(request, "products.html", {"products": products})
