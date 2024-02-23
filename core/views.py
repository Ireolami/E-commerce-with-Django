from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView, ListView
# Create your views here.
from django.db import IntegrityError
def index(request):
    products =Product.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'core/index.html', context)

#Search Panel
def search(request):
    if request.method == 'GET':
        searched = request.GET.get("query")
        if searched:
            items = Product.objects.filter(product_name__icontains=searched) 
            return render(request, 'core/searchpanel.html', {'items':items})
        else:
            print("No information to show")
            return render(request, 'core/searchpanel.html')
        


def store(request):
    return render(request, 'core/store.html')


def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals = []
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity  
        item_totals.append(item_total)
        total_price += item_total  
    item_with_total = zip(cart_items, item_totals)
    return render(request, 'core/checkout.html', {'item_with_total': item_with_total, 'total_price': total_price})

 

def product(request):
    return render(request, 'core/store.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def product_upload(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Product upload successfully')
            return redirect('index')

                             
    else:
        product_form = ProductForm()
    context = {'product_form': product_form}
    return render(request, 'core/product_upload.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'core/product_detail.html'
    context_object_name = 'product'
     
 
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    try:
        cart_item = CartItem.objects.get(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        try:
            cart_item = CartItem.objects.create(product=product, user=request.user, quantity=1)
        except IntegrityError as e:
            
            print(f"IntegrityError: {e}")
    
    
    return redirect('cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')   

def subtract_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item = get_object_or_404(CartItem, product=product, user=request.user)

    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()

    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals = []
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity  
        item_totals.append(item_total)
        total_price += item_total  
    item_with_total = zip(cart_items, item_totals)
    return render(request, 'core/cart.html', { 'total_price': total_price, 'item_with_total': item_with_total})


def increase_cart_quantity(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        pass
    
    return redirect('cart')