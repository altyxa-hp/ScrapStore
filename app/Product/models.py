from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(null=True)
    img_link = models.URLField(null=True)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

