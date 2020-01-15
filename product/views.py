from django.shortcuts import render, redirect
from . models import Product

# Create your views here.

def add_product(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		price = models.POST.get('price')
		product = Product.objects.create(name = name, price = price, quantity=0, user = request.user)
		product.save()
		return redirect('pages:dashboard')
	else:
		return redirect('pages:dashboard')

