# Generated by Django 3.1.7 on 2021-04-27 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_discount'),
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotions',
            name='ma_loai_san_pham',
            field=models.ForeignKey(db_column='ma_loai_san_pham', on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
