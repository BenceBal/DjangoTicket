# Generated by Django 4.2 on 2023-05-09 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_ek"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="ek",
        ),
    ]