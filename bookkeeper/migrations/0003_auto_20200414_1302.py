# Generated by Django 3.0.3 on 2020-04-14 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0002_auto_20200414_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='bookkeeper.Category'),
        ),
    ]
