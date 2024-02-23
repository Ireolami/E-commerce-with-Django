from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView
urlpatterns =[
    # path('', views.index, name='index'),
    path('', views.ProductListView.as_view(), name='index'),
    path('store/', views.store, name='store'),
    path('product', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'), 
    path('cart/', views.cart, name='cart'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('products_upload/', views.product_upload, name='products_upload'), 
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='detail'), 
    path('add-cart/<int:pk>/', views.add_to_cart, name='add-cart'), 
    path('subtract-cart/<int:pk>/', views.subtract_from_cart, name='subtract'), 
    path('remove-cart/<int:item_id>/', views.remove_from_cart, name='remove-cart'), 
    path('increase/<int:pk>/', views.increase_cart_quantity, name='increase'), 
]