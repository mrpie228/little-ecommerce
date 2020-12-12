from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=150,null=True)
    image = models.ImageField(blank=True,null=True,upload_to = 'static/images', )
    description= models.CharField(max_length=500,null=True)
    price= models.FloatField()
    in_stock= models.BooleanField(default=False, null=True,blank=False)
    quantity_in_stock=models.FloatField(default=0)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order= models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True,blank=False)
    transaction_id=models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total

    @property
    def get_total(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity= models.IntegerField(default=0,null=True,blank=True)
    date_added= models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total

class ShippingAdress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    adress= models.CharField(max_length=200,null=True)
    sity= models.CharField(max_length=200,null=True)
    zipcode= models.CharField(max_length=200,null=True)
    date_added= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.adress