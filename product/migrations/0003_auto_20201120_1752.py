# Generated by Django 3.1.3 on 2020-11-20 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201120_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
            preserve_default=False,
        ),
    ]
