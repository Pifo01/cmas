# Generated by Django 5.1.2 on 2024-11-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horario', models.DateTimeField()),
                ('Actividad', models.CharField(max_length=50)),
                ('Maquinas_Diponibles', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Metricas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Altura', models.IntegerField(max_length=3)),
                ('Peso', models.IntegerField(max_length=3)),
                ('Peso_press_banca', models.IntegerField(max_length=3)),
                ('Peso_press_inclinado', models.IntegerField(max_length=3)),
                ('Peso_fondos', models.IntegerField(max_length=3)),
                ('Peso_jalon_al_pecho', models.IntegerField(max_length=3)),
                ('Peso_remo_polea', models.IntegerField(max_length=3)),
                ('Peso_remo_libre', models.IntegerField(max_length=3)),
                ('Peso_dominada', models.IntegerField(max_length=3)),
                ('Peso_sentadilla_libre', models.IntegerField(max_length=3)),
                ('Peso_sentadilla_bulgara', models.IntegerField(max_length=3)),
                ('Peso_maquina_cuadriceps', models.IntegerField(max_length=3)),
                ('Peso_maquina_isquiotibiales', models.IntegerField(max_length=3)),
                ('Peso_gemelos', models.IntegerField(max_length=3)),
                ('Peso_biceps_mancuerna', models.IntegerField(max_length=3)),
                ('Peso_triceps_mancuerna', models.IntegerField(max_length=3)),
                ('Peso_elevaciones_laterales', models.IntegerField(max_length=3)),
                ('Peso_elevaciones_laterales_posterior', models.IntegerField(max_length=3)),
                ('Peso_press_militar', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('hora_entrada', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
