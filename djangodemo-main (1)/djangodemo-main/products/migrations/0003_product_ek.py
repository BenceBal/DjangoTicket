# Generated by Django 4.2 on 2023-05-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="ek",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
