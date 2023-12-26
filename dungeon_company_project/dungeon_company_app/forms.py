from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Импорт модели User
from .models import UserProfile, Product


class RegistrationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User  # Используйте модель User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['avatar']

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'game_rules', 'image']