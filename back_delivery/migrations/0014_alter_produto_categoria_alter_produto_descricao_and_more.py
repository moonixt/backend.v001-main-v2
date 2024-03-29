# Generated by Django 5.0.3 on 2024-03-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0013_alter_produto_categoria_alter_produto_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload/images'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
