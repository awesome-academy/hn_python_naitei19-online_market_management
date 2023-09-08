from django.shortcuts import render
from django.views import View, generic
from .models import Category
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class CategoryView(generic.DetailView):
    model=Category

    def get(self, request):
        menu = Category.objects.all()
        return render(request, 'catalog/menu.html', {'menu': menu})
