from django.views import View, generic
from .models import Category, Product, Cart, CartItem, CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import CustomUserForm
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from djmoney.money import Money

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
            messages.success(request, _('Changes saved'))
            return redirect('/profile')  # Sử dụng tên URL 'profile' để chuyển hướng

    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'registration/profile.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            cart = Cart.objects.create(user=user)
            cart.save()
            # Xử lý sau khi đăng ký thành công, ví dụ: chuyển hướng đến trang đăng nhập
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CartView(View):
    model=Cart

    def get(self, request):
        cartall = CartItem.objects.filter(cart_id=Cart.objects.get(user_id=request.user.id))
        total_price = sum(item.product.base_price * item.quantity for item in cartall)
        return render(request, 'catalog/cart.html',{'cartall':cartall,'total_price':total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa, nếu có thì tăng số lượng
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart')

def update_cart(request):

    if request.method == 'POST':
        action = request.POST.get('action')
        status = -1
        try:
            cart = CartItem.objects.get(id=request.POST.get("cart_item_id"))
            if (action=='increase'):
                cart.quantity += 1
            elif (action == 'decrease'):
                cart.quantity -= 1
            cart.save()
            status = 1
            if (action == 'delete') or (cart.quantity<1):
                cart.delete()
                status = 2
            cartall = CartItem.objects.filter(cart_id=Cart.objects.get(user_id=request.user.id))
            total_price = sum(item.product.base_price * item.quantity for item in cartall)
            return JsonResponse({'status':status,'message': 'Cập nhật giỏ hàng thành công', 'quantity': cart.quantity,'total_price':total_price})
            
        except Cart.DoesNotExist:
            return JsonResponse({'status':-1,'message': 'Sản phẩm không tồn tại'}, status=404)
    else:
        return JsonResponse({'status':-1,'message': 'Yêu cầu không hợp lệ'}, status=400)
