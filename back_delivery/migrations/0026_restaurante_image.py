# Generated by Django 4.2.7 on 2024-03-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0025_categoria_restaurantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload/images'),
        ),
    ]
