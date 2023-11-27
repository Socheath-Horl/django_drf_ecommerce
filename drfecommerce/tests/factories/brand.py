import factory

from drfecommerce.product.models import Brand


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brand"
