# Generated by Django 4.2.7 on 2023-11-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_productline"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
