# Generated by Django 4.2 on 2023-06-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_remove_order_order_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mesurement',
            old_name='order_quantity',
            new_name='jacket_order_quantity',
        ),
        migrations.AddField(
            model_name='mesurement',
            name='kurta_order_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mesurement',
            name='trouser_order_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
