# Generated by Django 4.2.6 on 2024-02-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketshop', '0016_alter_seasonticket_seasonticketid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonticket',
            name='seasonTicketid',
            field=models.CharField(default='B9BD4BF6D7', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]