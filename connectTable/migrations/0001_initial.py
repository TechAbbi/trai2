# Generated by Django 5.0.1 on 2024-01-18 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middel_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('model_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectTable.modela')),
                ('model_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectTable.modelb')),
            ],
        ),
    ]
