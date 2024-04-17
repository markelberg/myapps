# Generated by Django 5.0.4 on 2024-04-16 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_gestor', '0005_presupuestomensual_year_alter_presupuestomensual_mes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='presupuesto',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='gasto',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='gasto',
            name='categoria',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mi_gestor.categoria'),
        ),
    ]