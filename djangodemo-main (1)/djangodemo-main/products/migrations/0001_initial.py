# Generated by Django 4.2 on 2023-05-03 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'products_base',
                'swappable': 'PRODUCT_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.PRODUCT_MODEL)),
            ],
            options={
                'db_table': 'products_simple',
            },
            bases=('products.productbase',),
        ),
    ]
