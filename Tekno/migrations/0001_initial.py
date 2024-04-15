# Generated by Django 5.0.3 on 2024-04-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido1', models.CharField(max_length=15)),
                ('apellido2', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('cp', models.CharField(max_length=5)),
                ('dni', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('stock', models.CharField(default='hola', max_length=100)),
            ],
        ),
    ]