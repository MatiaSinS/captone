# Generated by Django 5.1.2 on 2024-12-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gotti', '0005_remove_carrito_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(related_name='carritos', to='Gotti.producto'),
        ),
    ]
