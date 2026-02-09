from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# functions or classes activate url go to and trigger

def home(request):
    # return HttpResponse('Home Page')
    return render(request,'accounts/dashboard.html')

def products(request):
    # return HttpResponse('Contact Page')
    return render(request,'accounts/products.html')

def customer(request):
    # return HttpResponse('Customer Page')
    return render(request, 'accounts/customer.html')