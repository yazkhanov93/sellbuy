from django.urls import path
from . import views


urlpatterns = [
	path('', views.sign_up, name='sign_up'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),
	#path('profile/', views.user_profile, name='profile'),
]