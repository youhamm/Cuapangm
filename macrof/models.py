from django.db import models

# Create your models here.

class Macro(models.Model):
	title = models.CharField(max_length=50)
	product = models.CharField(max_length=100)
	price = models.CharField(max_length=40)
	contents = models.CharField(max_length=500)
	product_i = models.CharField(max_length=1000)
	review = models.CharField(max_length=10000)
	link = models.CharField(max_length=500)

	def __str__(self):
		return self.product