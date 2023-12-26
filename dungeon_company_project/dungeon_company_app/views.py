# dungeon_company_app/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .forms import RegistrationForm, ProductCreationForm
from .models import Product, UserProfile


def about(request):
    return render(request, 'about.html')


def catalog(request):
    return render(request, 'catalog.html')


def home(request):
    latest_products = Product.objects.order_by('-id')[:5]
    return render(request, 'home.html', {'latest_products': latest_products})

class CatalogPageView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    ordering = ['name']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Создание профиля пользователя
            UserProfile.objects.create(user=user, avatar=form.cleaned_data['avatar'])

            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff

# Используем декоратор для ограничения доступа только для администраторов
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Измените 'index' на имя вашей домашней страницы
    else:
        form = ProductCreationForm()
    return render(request, 'add_product.html', {'form': form})

def search_results(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})