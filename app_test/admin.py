from django.contrib import admin
from app_test.models import Item


class ItemAdmin(admin.ModelAdmin):
	""" Product display in admin panel """
	list_display = ['id', 'name', 'description', 'price']


admin.site.register(Item, ItemAdmin)
