# Generated by Django 5.1.6 on 2025-03-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
