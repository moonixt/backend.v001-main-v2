# Generated by Django 5.0.3 on 2024-03-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0010_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(default=1, upload_to='upload/images'),
            preserve_default=False,
        ),
    ]
