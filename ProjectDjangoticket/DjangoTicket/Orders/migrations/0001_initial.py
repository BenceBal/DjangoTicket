# Generated by Django 4.2.5 on 2023-11-11 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ticketshop', '0001_initial'),
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Customers.shopcustomer')),
                ('seasonticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Ticketshop.seasonticket')),
                ('tickets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Ticketshop.myticket')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.PositiveIntegerField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_positions', to='Orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ticketshop.baseticket')),
            ],
            options={
                'unique_together': {('order', 'pos')},
            },
        ),
    ]