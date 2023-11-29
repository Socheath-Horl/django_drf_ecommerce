from django.db import models

from drfecommerce.product.models import Product


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=False)
