# Generated by Django 5.0.3 on 2024-04-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tekno', '0005_cliente_user_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=False),
        ),
    ]
