# Generated by Django 5.1.6 on 2025-02-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
    ]
