# Generated by Django 4.2 on 2023-05-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='credit',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
