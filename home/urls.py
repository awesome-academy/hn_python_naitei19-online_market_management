from django.urls import path
from .views import HomeView
from . import views
from django.contrib.auth.views import LoginView

app_name='home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('category/',views.CategoryView.as_view(), name='category'),
    path('accounts/login/', LoginView.as_view(), name='login'),
] 
