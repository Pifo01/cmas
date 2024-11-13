from django.db import models

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
class RegistroEntrada(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    hora_entrada = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} - {self.rut}"

class Metricas(models.Model):
    Altura=models.IntegerField(max_length=3)
    Peso=models.IntegerField(max_length=3)
    Peso_press_banca=models.IntegerField(max_length=3)
    Peso_press_inclinado=models.IntegerField(max_length=3)
    Peso_fondos=models.IntegerField(max_length=3)
    Peso_jalon_al_pecho=models.IntegerField(max_length=3)
    Peso_remo_polea=models.IntegerField(max_length=3)
    Peso_remo_libre=models.IntegerField(max_length=3)
    Peso_dominada=models.IntegerField(max_length=3)
    Peso_sentadilla_libre=models.IntegerField(max_length=3)
    Peso_sentadilla_bulgara=models.IntegerField(max_length=3)
    Peso_maquina_cuadriceps=models.IntegerField(max_length=3)
    Peso_maquina_isquiotibiales=models.IntegerField(max_length=3)
    Peso_gemelos=models.IntegerField(max_length=3)
    Peso_biceps_mancuerna=models.IntegerField(max_length=3)
    Peso_triceps_mancuerna=models.IntegerField(max_length=3)
    Peso_elevaciones_laterales=models.IntegerField(max_length=3)
    Peso_elevaciones_laterales_posterior=models.IntegerField(max_length=3)
    Peso_press_militar=models.IntegerField(max_length=3)

class Clases(models.Model):
    Horario = models.CharField(max_length=50)
    Actividad = models.CharField(max_length=50)
    Maquinas_Diponibles = models.CharField(max_length=50)