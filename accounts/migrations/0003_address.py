# Generated by Django 4.1.3 on 2023-04-12 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone1', models.CharField(default=0, max_length=15)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('phone2', models.CharField(default=0, max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
