from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'profile.html')

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'product_list.html')


def product_detail(request):
    return render(request, 'product_detail.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def checkout(request):
    return render(request, 'checkout.html')

def orders(request):
    return render(request, 'orders.html')