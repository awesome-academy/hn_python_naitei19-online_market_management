
from django.test import TestCase
from home.models import Category
from ..forms import CustomUserForm, RegistrationForm, CategoryForm, ProductForm, ADCustomUserForm, CustomUserDetailForm

class FormsTestCase(TestCase):
    def test_custom_user_form(self):
        form_data = {
            'first_name': 'Huy',
            'last_name': 'Le',
            'email': 'huyle@example.com',
            'phone': '1234567890',
            'address': '123 Ha Noi',
        }
        form = CustomUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'mypassword123',
            'password2': 'mypassword123',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form(self):
        category = Category.objects.create(name='Test Category')
        form_data = {
            'name': 'New Category',
            'parent': category.pk,
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form(self):
        category = Category.objects.create(name='Test Category')
        form_data = {
            'name': 'New Product',
            'category': category.pk,
            'image': 'product.jpg',
            'description': 'A new product',
            'base_price': 10,
            'number_in_stock': 20,
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ad_custom_user_form(self):
        form_data = {
            'username': 'newuser',
            'password1': 'mypassword123',
            'password2': 'mypassword123',
        }
        form = ADCustomUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_detail_form(self):
        form_data = {
            'username': 'HuyQL',
            'first_name': 'Le',
            'last_name': 'Quang Huy',
            'email': 'leekanghye2002@gmail.com',
            'phone': '1234567890',
            'address': '123 Ha Noi',
            'is_staff': True,
        }
        form = CustomUserDetailForm(data=form_data)
        self.assertTrue(form.is_valid())
