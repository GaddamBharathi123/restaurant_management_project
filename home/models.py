from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    def_str_(self):
        return self.user.username

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()

    def_str_(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [('PENDING','pending'),('CONFIRMED','confirmed'),('DELIVERED','delivered'),('CANCELLED','cancelled'),]
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    order_items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    order_status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def_str_(self):
        return f"Order#{self.id} by {self.customer.username}"
