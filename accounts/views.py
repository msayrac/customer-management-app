from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# functions or classes activate url go to and trigger

def home(request):
    return HttpResponse('Home Page')

def products(request):
    return HttpResponse('Contact Page')

def customer(request):
    return HttpResponse('Customer Page')