# Generated by Django 2.2 on 2023-02-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
