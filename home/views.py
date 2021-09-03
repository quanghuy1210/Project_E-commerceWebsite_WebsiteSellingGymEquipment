from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

# Create your views here.
def getHomeView(request):
    return render(request, 'home/index.html') 
    #return HttpResponse('<h1>Hi</h1>')

def getCartView(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request, 'cart.html', {'products': products})