from __future__ import unicode_literals
from django.db import models


class Cars(models.Model):
    pic = models.CharField(max_length=1000, default=" ")
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    launch_date = models.DateField(default=0-0-0)
    about = models.TextField(default=" ")

    def __str__(self):
        return self.company + '-' + self.name


class UsedCars(models.Model):
    company = models.CharField(max_length=500)
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    driven = models.IntegerField(default=0)
    oil = models.CharField(max_length=100)
    owner_type = models.CharField(max_length=100)
    place = models.CharField(max_length=500)
    pic = models.FileField(default=None)

    def __str__(self):
        return self.company + self.name + '-' + self.place


class Owner(models.Model):
    car = models.ForeignKey(UsedCars, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    mobile_no = models.IntegerField(default=0)

    def __str__(self):
        return self.name + '-' + self.car.company + self.car.name + '-' + self.car.place

