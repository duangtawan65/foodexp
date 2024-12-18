from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# รายละเอียดสินค้า
class FoodItem(models.Model):
    name = models.CharField(max_length=100)  # ชื่อสินค้า
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    expiry_date = models.DateField()  # วันหมดอายุ

    def __str__(self):
        return f"{self.name} ({self.category.name})"