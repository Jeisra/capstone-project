# Generated by Django 5.1.5 on 2025-01-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_menu_menu_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
