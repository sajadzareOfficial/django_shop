# Generated by Django 5.1.7 on 2025-04-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsoolat', '0003_mahsoolat_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsoolat',
            name='Category',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='mahsoolat',
            name='hafezeh',
            field=models.CharField(default=10, max_length=7),
        ),
        migrations.AddField(
            model_name='mahsoolat',
            name='product_type',
            field=models.CharField(choices=[('phone', 'گوشی'), ('tablet', 'تبلت'), ('console', 'کنسول'), ('laptop', 'لپتاپ'), ('accessory', 'لوازم جانبی')], default=None, max_length=20),
        ),
    ]
