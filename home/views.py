from django.views import View, generic
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class HomeView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')

class CategoryView(generic.DetailView):
    model=Category

    def get(self, request):
        menu = Category.objects.all()
        products = Product.objects.all()
        return render(request, 'catalog/menu.html', {'menu': menu,'products' : products})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Changes Saved'))
            return redirect('/profile')  # Sử dụng tên URL 'profile' để chuyển hướng

    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'registration/profile.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')
