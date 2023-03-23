# Generated by Django 4.1.7 on 2023-03-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_pishiriqlar_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slayder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Slayder sarlavhasi')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Slayder',
            },
        ),
    ]
