
from django.test import TestCase
from ..models import CustomUser, Category, Product, Order, OrderDetail, Cart, CartItem, BestSeller, Promotion
from django.utils import timezone

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1', phone='1234567890', address='123 Ha Noi')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', description='Test Description', base_price=10, number_in_stock=5, category=self.category)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(quantity=2, cart=self.cart, product=self.product)
        self.order = Order.objects.create(order_date=timezone.now(), status=0, user=self.user, cart=self.cart, order_cost=20)
        self.order_detail = OrderDetail.objects.create(price=10, quantity=2, order=self.order, product=self.product, total_cost=20)
        self.best_seller = BestSeller.objects.create(product=self.product, sold_number=10)
        self.promotion = Promotion.objects.create(product=self.product, description='Test Promotion', dis_percent=10, start_date=timezone.now(), end_date=timezone.now())

    def test_custom_user_creation(self):
        self.assertEqual(self.user.phone, '1234567890')
        self.assertEqual(self.user.address, '123 Ha Noi')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.is_available(), True)
        self.assertEqual(self.product.get_stock_count(), 5)

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(self.cart_item.cart, self.cart)

    def test_order_creation(self):
        self.assertEqual(self.order.status, 0)
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.cart, self.cart)
        self.assertEqual(self.order.order_cost, 20)

    def test_order_detail_creation(self):
        self.assertEqual(self.order_detail.price, 10)
        self.assertEqual(self.order_detail.quantity, 2)
        self.assertEqual(self.order_detail.order, self.order)
        self.assertEqual(self.order_detail.product, self.product)
        self.assertEqual(self.order_detail.total_cost, 20)

    def test_best_seller_creation(self):
        self.assertEqual(self.best_seller.sold_number, 10)

    def test_promotion_creation(self):
        self.assertEqual(self.promotion.description, 'Test Promotion')
        self.assertEqual(self.promotion.dis_percent, 10)
