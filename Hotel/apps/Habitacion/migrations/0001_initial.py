# Generated by Django 2.0.7 on 2018-07-05 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('idHabitacion', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(default=0)),
                ('estado', models.BooleanField(default=False)),
                ('costo', models.IntegerField(default=0)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
