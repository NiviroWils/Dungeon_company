# dungeon_company_app/urls.py

from django.urls import path
from . import views
from .views import ProductDetailView, CatalogPageView, register, user_logout, user_login, profile, \
    add_product, home, search_results, order_product

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', CatalogPageView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('add_product/', add_product, name='add_product'),
    path('search_result/', search_results, name='search_results'),
    path('order/<int:product_id>/', order_product, name='order_product'),
]
