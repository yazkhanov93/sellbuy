from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Q
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def category_list(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	product = Product.objects.filter(category=category)
	return render(request, 'category.html', {'category': category, 'product': product})



def home_page(request):
	search = request.GET.get('search', '')
	if search:
		product = Product.objects.filter(Q(name__icontains=search)|Q(description__icontains=search))
	else:
		product = Product.objects.all()
	return render(request, 'home.html', {'product': product})



def product_detail(request, pk):
	product_detail = get_object_or_404(Product, id=pk)
	return render(request, 'detail.html', {'product_detail': product_detail})


@login_required(login_url='login')
def add_post(request):
	form = ProductForm()
	user = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.author = user
			obj.save()
			return redirect('/')
	return render(request, 'form.html', {'form': form}) 



def edit_post(request, pk):
	post = Product.objects.get(id=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
			return redirect('profile')
	return render(request, 'form.html', {'post': post, 'form': ProductForm(instance=post)})



def delete_post(request, pk):
	post = Product.objects.get(id=pk)
	post.delete()
	return redirect('profile')



def user_profile(request):
	post = Product.objects.filter(author=request.user)
	return render(request, 'profile.html', {'post': post})


