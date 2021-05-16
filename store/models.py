from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse



class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)


	class Meta:
		verbose_name_plural = 'categories'


	def get_absolute_url(self):
		return reverse('category_list', args=[self.slug])

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	img = models.ImageField(upload_to='img/')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	published = models.DateTimeField(auto_now=True)
	description = models.TextField()
	phone = models.CharField(max_length=12)
	region = models.CharField(max_length=255)


	class Meta:
		ordering = ('-published',)


	def __str__(self):
		return self.name



