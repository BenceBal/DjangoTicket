# Generated by Django 4.2.6 on 2024-02-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketshop', '0019_alter_seasonticket_seasonticketid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonticket',
            name='seasonTicketid',
            field=models.CharField(default='2879A02960', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]