# Generated by Django 3.1.3 on 2020-11-22 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20201122_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalproduct',
            name='main_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='product.productdetail'),
        ),
        migrations.AlterField(
            model_name='additionalproduct',
            name='sub_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='product.productdetail'),
        ),
    ]