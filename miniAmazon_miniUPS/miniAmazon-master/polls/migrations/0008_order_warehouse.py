# Generated by Django 4.0.1 on 2022-04-14 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_initializedflag_inventory_order_product_warehouse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.warehouse'),
        ),
    ]
