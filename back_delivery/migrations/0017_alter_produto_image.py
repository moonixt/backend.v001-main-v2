# Generated by Django 5.0.3 on 2024-03-20 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0016_alter_produto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/images'),
        ),
    ]
