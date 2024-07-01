from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    




class Useregister(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
    


