# Generated by Django 5.1.2 on 2024-11-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortalCMAS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetricasCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.IntegerField(null=True)),
                ('peso', models.IntegerField(null=True)),
                ('horas_entrenadas', models.IntegerField(null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('rut_cliente', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetricasTrenInferior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_sentadilla_libre', models.IntegerField(null=True)),
                ('peso_sentadilla_bulgara', models.IntegerField(null=True)),
                ('peso_maquina_cuadriceps', models.IntegerField(null=True)),
                ('peso_maquina_isquiotibiales', models.IntegerField(null=True)),
                ('peso_gemelos', models.IntegerField(null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('rut_cliente', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetricasTrenSuperior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_press_banca', models.IntegerField(null=True)),
                ('peso_press_inclinado', models.IntegerField(null=True)),
                ('peso_fondos', models.IntegerField(null=True)),
                ('peso_jalon_al_pecho', models.IntegerField(null=True)),
                ('peso_remo_polea', models.IntegerField(null=True)),
                ('peso_remo_libre', models.IntegerField(null=True)),
                ('peso_dominada', models.IntegerField(null=True)),
                ('peso_biceps_mancuerna', models.IntegerField(null=True)),
                ('peso_triceps_mancuerna', models.IntegerField(null=True)),
                ('peso_elevaciones_laterales', models.IntegerField(null=True)),
                ('peso_elevaciones_laterales_posterior', models.IntegerField(null=True)),
                ('peso_press_militar', models.IntegerField(null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('rut_cliente', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Metricas',
        ),
    ]
