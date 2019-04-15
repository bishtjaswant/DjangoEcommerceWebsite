from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,"shop/index.html")


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
