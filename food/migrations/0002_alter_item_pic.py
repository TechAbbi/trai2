# Generated by Django 5.0.1 on 2024-01-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS6Pq0Qe0oXY4wFa1hl-W3b1lrFfI0OXy3E2XaUnupF0O2b7MvmlzhnSLl-g&s', max_length=5000),
        ),
    ]
