# Generated by Django 5.2 on 2025-04-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahsoolat', '0017_mahsoolat_reagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahsoolat',
            name='Category',
        ),
        migrations.AddField(
            model_name='mahsoolat',
            name='Rom',
            field=models.CharField(default='usa', max_length=10),
        ),
    ]
