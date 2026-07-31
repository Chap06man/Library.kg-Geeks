from django.db import models
# Create your models here.

#Категории магазина
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
#Продукты магазина
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category_product = models.ForeignKey(Category,blank=True, null=True, on_delete=models.CASCADE)#связ 

    def __str__(self):
        return f"{self.name} - {self.price} сом - {self.category_product}"

    
