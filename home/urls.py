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
    # URL cho quản lý thống kê
    path('admin/overview/', views.overview, name='admin_overview'),
    # URL cho quản lý thể loại sản phẩm
    path('admin/categories/', views.admin_category_list, name='admin_category_list'),
    path('delete_categories/', views.delete_categories, name='delete_categories'),
    path('admin/categories/create/', views.admin_category_create, name='admin_category_create'),
    path('admin/categories/<int:category_id>/update/', views.admin_category_update, name='admin_category_update'),
    # URL cho quản lý sản phẩm
    path('admin/products/', views.admin_product_list, name='admin_product_list'),
    path('admin/products/create/', views.admin_product_create, name='admin_product_create'),
    path('admin/products/<int:product_id>/update/', views.admin_product_update, name='admin_product_update'),
]
