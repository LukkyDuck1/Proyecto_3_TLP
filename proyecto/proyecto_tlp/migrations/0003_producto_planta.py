# Generated by Django 5.0.6 on 2024-07-07 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_tlp', '0002_registroproduccion_fecha_modificacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='planta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='proyecto_tlp.planta'),
        ),
    ]
