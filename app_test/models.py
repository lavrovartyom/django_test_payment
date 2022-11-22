from django.db import models


class Item(models.Model):
	""" Product model """
	name = models.CharField(max_length=70, verbose_name='product name')
	description = models.TextField(verbose_name='product description')
	price = models.IntegerField(default=0, verbose_name='the price of the product')

	def __str__(self):
		return self.name


