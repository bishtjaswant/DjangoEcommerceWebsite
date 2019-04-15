from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    product = Product.objects.all()
    n = len(product)

    num_of_slide = n//4 + ceil( (n//4 - n/4))

    print(num_of_slide)
    return render(request,"shop/index.html", {'product':product, 'num_of_slide': num_of_slide, 'range': range(1, num_of_slide) })


def aboutus(request):
    return render(request,"shop/aboutus.html")


def contactus(request):
    return render(request,"shop/contactus.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def products(request):
    return render(request,"shop/products.html")

def checkout(request):
    return render(request,"shop/checkout.html")
