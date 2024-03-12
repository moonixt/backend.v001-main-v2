# Generated by Django 5.0.2 on 2024-03-03 23:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_delivery', '0002_usuario_groups_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_nota_fiscal', models.IntegerField()),
                ('serie_nota_fiscal', models.IntegerField()),
                ('data_compra', models.DateTimeField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd_total', models.IntegerField()),
                ('pedido_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
