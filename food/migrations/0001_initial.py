# Generated by Django 5.0.1 on 2024-01-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('pic', models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS6Pq0Qe0oXY4wFa1hl-W3b1lrFfI0OXy3E2XaUnupF0O2b7MvmlzhnSLl-g&s', max_length=1000)),
            ],
        ),
    ]
