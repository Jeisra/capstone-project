# Generated by Django 5.1.5 on 2025-01-29 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_delete_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
