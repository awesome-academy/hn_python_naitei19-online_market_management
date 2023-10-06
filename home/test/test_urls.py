from django.test import TestCase
from django.urls import reverse

class UrlsTestCase(TestCase):
    def test_category_url(self):
        url = reverse('home:category')
        self.assertEqual(url, '/category/')

    def test_home_url(self):
        url = reverse('home:home')
        self.assertEqual(url, '/home/')

    # Tiếp tục kiểm tra cho các URL khác

    def test_admin_order_url(self):
        url = reverse('home:admin_order')
        self.assertEqual(url, '/admin/order/')

    def test_admin_category_list_url(self):
        url = reverse('home:admin_category_list')
        self.assertEqual(url, '/admin/categories/')

    # Tiếp tục kiểm tra cho các URL quản lý thể loại sản phẩm và sản phẩm khác

    def test_admin_user_list_url(self):
        url = reverse('home:admin_user_list')
        self.assertEqual(url, '/admin/users/')

    def test_admin_statistics_url(self):
        url = reverse('home:admin_statistics')
        self.assertEqual(url, '/admin/statistics/')
