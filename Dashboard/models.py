from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username + '-Customer'

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.customer + ' - ' + str(self.created_at)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username + '-Company'

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 1000)
    price = models.FloatField()
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('Dashboard:a')

    def __str__(self):
        return self.name + ' - ' + str(self.price) + ' - ' + str(self.pk)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.OneToOneField(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name + ' - ' + self.quantity