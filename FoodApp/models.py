from django.db import models

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