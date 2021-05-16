from django.urls import path
from . import views



urlpatterns = [
	path('', views.home_page, name='home_page' ),
	path('search/<slug:category_slug>/', views.category_list, name='category_list'),
	path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
	path('add_post/', views.add_post, name='add_post'),
	path('profile/', views.user_profile, name='profile'),
	path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
	path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
]