# Generated by Django 4.2.7 on 2024-03-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0026_restaurante_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='descricao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
