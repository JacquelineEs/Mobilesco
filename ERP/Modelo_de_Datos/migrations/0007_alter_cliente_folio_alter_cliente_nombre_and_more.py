# Generated by Django 5.1.3 on 2024-11-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelo_de_Datos', '0006_cliente_hoja_de_presupuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='folio',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hoja_de_presupuesto',
            name='folio_pres',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='hoja_de_presupuesto',
            name='presupuesto',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
