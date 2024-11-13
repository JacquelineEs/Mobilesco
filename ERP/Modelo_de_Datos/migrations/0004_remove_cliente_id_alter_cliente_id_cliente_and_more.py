# Generated by Django 5.0.9 on 2024-11-12 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo_de_Datos', '0003_cliente_hoja_de_presupuesto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hoja_de_presupuesto',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modelo_de_Datos.cliente'),
        ),
    ]