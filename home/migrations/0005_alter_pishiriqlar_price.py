# Generated by Django 4.1.7 on 2023-03-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_slayder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pishiriqlar',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
