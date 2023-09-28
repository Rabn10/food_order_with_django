from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cname=models.TextField(max_length=20,primary_key=True)
    def __str__(self):
        return self.cname
    
class FoodItem(models.Model):
    name=models.TextField(max_length=40)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.TextField(max_length=100,default="its juicy")
    pimage=models.ImageField(upload_to="restaurant/images",default="")
    price=models.IntegerField()
    totalOrders=models.IntegerField(default=0)
    rating=models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.TextField(max_length=200)
    email = models.TextField(max_length=200,unique=True)
    phone_no = models.TextField(max_length=40)
    password = models.TextField(max_length=200)
    c_password = models.TextField(max_length=200)
    def _str_(self):
        return self.name
    

class tlb_order(models.Model):
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id')
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    process_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')


class tbl_order_details(models.Model):
    order_id = models.ForeignKey(tlb_order, on_delete=models.CASCADE, to_field='id')
    menu_id = models.ForeignKey(FoodItem, on_delete=models.CASCADE, to_field='id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_orders = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order ID: {self.order_id.id}, Menu ID: {self.menu_id.id}"

class tbl_payment(models.Model):
    order = models.ForeignKey(tlb_order, on_delete=models.CASCADE, to_field='id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.TextField(max_length=200)
    payment_date = models.DateField()   
    process_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')   


class tbl_rating(models.Model):
    menu = models.ForeignKey(FoodItem, on_delete=models.CASCADE, to_field='id')
    score = models.IntegerField(default=0)
    remarks = models.TextField(max_length=200)
    date_recorded = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='id')

    def _str_(self):
        return self.customer
