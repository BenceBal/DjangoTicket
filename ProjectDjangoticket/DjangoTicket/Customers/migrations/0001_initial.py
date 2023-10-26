# Generated by Django 4.2.6 on 2023-10-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCustomer',
            fields=[
                ('personalid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('joined', models.DateField(auto_now_add=True)),
                ('fanClubMember', models.BooleanField(default=False)),
                ('fanClubMemberid', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]