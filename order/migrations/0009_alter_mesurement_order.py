# Generated by Django 4.2 on 2023-05-28 18:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_mesurement_id_alter_mesurement_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesurement',
            name='order',
            field=models.OneToOneField(blank=True, default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='order.order'),
        ),
    ]
