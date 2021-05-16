from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from store.models import Product
from django.contrib.auth.models import User



# user sign up function
def sign_up(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			forms = UserCreationForm()
	return render(request, 'sign_up.html', {'form': form})



# user login function
def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/')
		else:
			messages.info(request, 'something went wrong, check username or password...!')
	context = {}
	return render(request, 'login.html', context)


#logout function
def logout_page(request):
	logout(request)
	return redirect('login')


# user profile page
"""
def user_profile(request):
	product = Product.objects.filter(user=request.author)
	return render(request, 'profile.html', {'product': product})
"""