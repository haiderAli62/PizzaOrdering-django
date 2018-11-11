from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topping(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"with {self.name} topping"



class Regular_Pizza(models.Model):
	pizza_type = models.CharField(max_length=64)
	small = models.DecimalField(max_digits=5, decimal_places=2)
	large = models.DecimalField(max_digits=5, decimal_places=2) 

	def __str__(self):
		return f"Selected {self.pizza_type} "

class Sicilian_Pizza(models.Model):
	pizza_type = models.CharField(max_length=64 ,  default=None)
	small = models.DecimalField(max_digits=5, decimal_places=2 , default=None)
	large = models.DecimalField(max_digits=5, decimal_places=2 , default=None)  


	def __str__(self):
		return f"Selected {self.pizza_type} "

class Cart(models.Model):
	item = models.CharField(max_length=64)
	size = models.DecimalField(max_digits=5,decimal_places=2)
	extras = models.CharField(max_length=64 , null=True, blank=True)
	user = models.ManyToManyField(User , related_name="member")

class Orders(models.Model):
	item = models.CharField(max_length=64)
	size = models.DecimalField(max_digits=5,decimal_places=2)
	extras = models.CharField(max_length=64 , null=True, blank=True)
	user = models.ManyToManyField(User , related_name="customer")





	













