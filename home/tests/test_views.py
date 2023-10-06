from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Product, Cart, CartItem, CustomUser, Order, Promotion
from ..views import filter_promotion
import datetime

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            category=self.category,
            base_price=10.0,
            number_in_stock=100
        )
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_home_view(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')

    def test_category_view(self):
        response = self.client.get(reverse('home:category'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/menu.html')

    def test_update_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')

    def test_custom_logout_view(self):
        response = self.client.get(reverse('home:custom_logout'))
        self.assertEqual(response.status_code, 302) 

    def test_register_view(self):
        response = self.client.get(reverse('home:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home:cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/cart.html')

    def test_add_to_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home:add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_update_cart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('home:update_cart'), {'action': 'increase', 'cart_item_id': self.cart_item.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 1)  

    def test_add_order_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('home:add_order'))
        self.assertEqual(response.status_code, 302)  


    def test_filter_promotion(self):
        today = datetime.date.today()
        promotion = Promotion.objects.create(
            product=self.product,
            dis_percent=10,
            description='Test Promotion',
            start_date=today - datetime.timedelta(days=1),
            end_date=today + datetime.timedelta(days=1)
        )
        promotions = filter_promotion(self.product)
        self.assertTrue(promotions.exists())
