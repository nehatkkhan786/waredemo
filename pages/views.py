from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def deshboard(request):
	return render(request, 'dashboard.html')


def login(request):
	if request.method == 'POST':
		# Get Form Values 
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = auth.authenticate(email = email, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('pages:dashboard')
		else:
			return redirect('pages:login')
	return render(request, 'login.html', )
