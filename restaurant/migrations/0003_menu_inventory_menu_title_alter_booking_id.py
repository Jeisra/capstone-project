# Generated by Django 5.1.5 on 2025-01-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_name_booking_name_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='Default Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
