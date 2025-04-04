# Generated by Django 5.1.6 on 2025-03-30 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_alter_coupon_code_alter_orderitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='total_discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default='CA28D720', max_length=30, unique=True),
        ),
    ]
