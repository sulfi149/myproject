# Generated by Django 4.1.4 on 2023-04-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Order_day',
            field=models.IntegerField(default=21),
        ),
        migrations.AddField(
            model_name='order',
            name='Order_month',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='order',
            name='Order_year',
            field=models.IntegerField(default=2023),
        ),
    ]