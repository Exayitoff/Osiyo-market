# Generated by Django 4.1.7 on 2023-03-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elektronika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('image', models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')),
                ('about', models.TextField(verbose_name="Ma'lumot")),
            ],
            options={
                'verbose_name_plural': 'Elektronika',
            },
        ),
        migrations.CreateModel(
            name='Pishiriqlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('image', models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')),
                ('about', models.TextField(verbose_name="Ma'lumot")),
            ],
            options={
                'verbose_name_plural': 'Pishiriqlar',
            },
        ),
        migrations.CreateModel(
            name='Sigaret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(verbose_name='Narxi')),
                ('image', models.ImageField(upload_to='rasmlar/', verbose_name='Rasmi')),
                ('about', models.TextField(verbose_name="Ma'lumot")),
            ],
            options={
                'verbose_name_plural': 'Sigaret',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategoriya'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
