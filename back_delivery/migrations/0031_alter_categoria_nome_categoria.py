# Generated by Django 4.2.7 on 2024-03-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0030_remove_categoria_restaurantes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_categoria',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]