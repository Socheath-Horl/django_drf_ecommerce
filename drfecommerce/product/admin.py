from django.contrib import admin

from drfecommerce.product.models import Brand, Category, Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
