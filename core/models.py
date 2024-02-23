from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    minimum_order = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_pics', default=None)

    def __str__(self):
        return self.product_name
    
    @property
    def discount(self):
        return self.price * 0.8
    
    
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} * {self.product}"
    
   