from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home(request):

 return render(request, 'crm/home.html')

def shop(request):

 return render(request, 'crm/shop.html')

def pricing(request):

 return render(request, 'crm/pricing.html')

def cart(request):

 return render(request, 'crm/cart.html')

def signin(request):

 return render(request, 'crm/signin.html')

def signup(request):

 return render(request, 'crm/signup.html')