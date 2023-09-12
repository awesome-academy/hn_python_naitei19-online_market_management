from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']  # Chọn các trường bạn muốn cập nhật
