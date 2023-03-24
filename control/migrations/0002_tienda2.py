# Generated by Django 4.1.7 on 2023-03-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tienda', models.CharField(max_length=50)),
                ('layer_code', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_actual', models.DateField(auto_now_add=True)),
                ('dias', models.IntegerField()),
            ],
        ),
    ]