from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    #Uses the Products Model
    #the form has a name q you will see q referred to again in base.html
    #whatever is typed into the form is used to filter the products
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})