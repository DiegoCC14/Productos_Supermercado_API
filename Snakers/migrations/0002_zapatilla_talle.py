# Generated by Django 5.0.7 on 2024-08-01 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapatilla_Talle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.FloatField()),
                ('zapatilla_talle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snakers.zapatillas')),
            ],
        ),
    ]
