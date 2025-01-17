# Generated by Django 5.0.6 on 2024-07-07 01:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_produccion', models.DateField()),
                ('turno', models.CharField(choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], max_length=2)),
                ('hora_registro', models.DateTimeField(auto_now_add=True)),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto_tlp.planta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto_tlp.producto')),
            ],
        ),
    ]
