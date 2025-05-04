from django.db import models

# Create your models here.


class Customer(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)


class Order(models.Model):
    product=models.CharField(max_length=100)
    quantity=models.IntegerField()
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='orders')