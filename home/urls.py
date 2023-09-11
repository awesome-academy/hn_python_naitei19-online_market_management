from django.urls import path
from .views import HomeView
from . import views

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('category/',views.CategoryView.as_view(), name='category'),
    path('home/', HomeView.as_view(), name='home'),

] 
