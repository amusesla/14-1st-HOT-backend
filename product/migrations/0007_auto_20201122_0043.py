# Generated by Django 3.1.3 on 2020-11-21 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20201122_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.size'),
        ),
    ]
