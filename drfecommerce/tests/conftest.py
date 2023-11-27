from pytest_factoryboy import register

from drfecommerce.tests.factories import (BrandFactory, CategoryFactory,
                                          ProductFactory)

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
