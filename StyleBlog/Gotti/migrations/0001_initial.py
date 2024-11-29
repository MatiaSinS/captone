# Generated by Django 5.1.2 on 2024-11-25 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('idDatoPersonal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('correoElectronico', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BarberoPendiente',
            fields=[
                ('idBarberoPendiente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('correoElectronico', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=100)),
                ('horario', models.DateField()),
                ('aprobado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('reservado', models.BooleanField(default=False)),
                ('confirmado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.FloatField(max_length=10)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombreServicio', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.FloatField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='servicios/')),
            ],
        ),
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('datospersonales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Gotti.datospersonales')),
                ('idBarbero', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=100)),
                ('horario', models.DateField()),
                ('telefono', models.CharField(max_length=15)),
            ],
            bases=('Gotti.datospersonales',),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('datospersonales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Gotti.datospersonales')),
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=15)),
            ],
            bases=('Gotti.datospersonales',),
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito_productos', to='Gotti.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gotti.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(related_name='carritos', to='Gotti.producto'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gotti.cliente'),
        ),
        migrations.CreateModel(
            name='BloqueHorario',
            fields=[
                ('idbloque', models.AutoField(primary_key=True, serialize=False)),
                ('horarioinicio', models.TimeField()),
                ('horariofin', models.TimeField()),
                ('fecha', models.DateField()),
                ('disponibilidad', models.CharField(default='DISPONIBLE', max_length=20)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gotti.servicio')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gotti.cliente')),
            ],
        ),
    ]
