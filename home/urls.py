from django.urls import path
from .views import HomeView
from . import views
from django.contrib.auth.views import LoginView

app_name='home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('category/',views.CategoryView.as_view(), name='category'),
    path('cart/',views.CartView.as_view(), name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('profile/', views.update_profile, name='profile'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),
]
