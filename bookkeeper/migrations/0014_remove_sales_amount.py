# Generated by Django 3.0.3 on 2020-04-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0013_sales_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='amount',
        ),
    ]
