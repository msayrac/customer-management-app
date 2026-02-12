from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# functions or classes activate url go to and trigger

def home(request):
    orders =Order.objects.all()
    customers = Customer.objects.all()
    context = {'orders':orders, 'customers':customers}
    # return HttpResponse('Home Page')
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    # return HttpResponse('Contact Page')
    return render(request,'accounts/products.html', {'products':products})

def customer(request):
    # return HttpResponse('Customer Page')
    return render(request, 'accounts/customer.html')