# Generated by Django 5.1.6 on 2025-03-19 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_categoryoffer_offer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryoffer',
            old_name='category',
            new_name='name',
        ),
    ]
