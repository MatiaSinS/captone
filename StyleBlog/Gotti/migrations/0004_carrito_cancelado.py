# Generated by Django 5.1.2 on 2024-12-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gotti', '0003_alter_barbero_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
