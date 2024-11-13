# Generated by Django 5.1.3 on 2024-11-13 18:07

import django.db.models.deletion
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
                ('folio', models.TextField(max_length=250)),
                ('nombre', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('position', models.TextField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hoja_de_Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_pres', models.TextField(max_length=250)),
                ('presupuesto', models.TextField(max_length=250)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modelo_de_Datos.cliente')),
            ],
        ),
    ]
