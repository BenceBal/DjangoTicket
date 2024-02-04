# Generated by Django 4.2.6 on 2024-02-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketshop', '0013_alter_seasonticket_seasonticketid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchstadium',
            old_name='sector',
            new_name='section',
        ),
        migrations.RemoveField(
            model_name='matchstadium',
            name='capacityFanSector',
        ),
        migrations.AlterField(
            model_name='seasonticket',
            name='seasonTicketid',
            field=models.CharField(default='75E514839D', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]