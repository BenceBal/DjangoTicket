# Generated by Django 4.2.6 on 2024-02-03 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ticketshop', '0007_alter_seasonticket_seasonticketid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='match',
            name='capacityFanSector',
        ),
        migrations.RemoveField(
            model_name='match',
            name='sector',
        ),
        migrations.AlterField(
            model_name='seasonticket',
            name='seasonTicketid',
            field=models.CharField(default='90AE548076', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='MatchStadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=30)),
                ('capacityFanSector', models.IntegerField(default=10)),
                ('sector', models.CharField(default='A', max_length=2)),
                ('matchname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ticketshop.match')),
            ],
        ),
        migrations.AlterField(
            model_name='myticket',
            name='matchEvent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Ticketshop.matchstadium'),
        ),
    ]
