# Generated by Django 5.0.4 on 2024-04-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_gestor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gasto',
            old_name='monto',
            new_name='cantidad',
        ),
        migrations.RenameField(
            model_name='presupuestomensual',
            old_name='monto',
            new_name='cantidad',
        ),
    ]
