# Generated by Django 3.1.3 on 2020-11-25 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201125_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartbox',
            name='seller',
        ),
    ]