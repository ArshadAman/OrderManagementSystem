# Generated by Django 4.2 on 2023-05-28 18:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_mesurement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mesurement',
            name='order',
            field=models.OneToOneField(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.order'),
        ),
    ]