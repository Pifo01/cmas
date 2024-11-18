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
    altura = models.IntegerField(null=True)
    peso = models.IntegerField(null=True)
    peso_press_banca = models.IntegerField(null=True)
    peso_press_inclinado = models.IntegerField(null=True)
    peso_fondos = models.IntegerField(null=True)
    peso_jalon_al_pecho = models.IntegerField(null=True)
    peso_remo_polea = models.IntegerField(null=True)
    peso_remo_libre = models.IntegerField(null=True)
    peso_dominada = models.IntegerField(null=True)
    peso_sentadilla_libre = models.IntegerField(null=True)
    peso_sentadilla_bulgara = models.IntegerField(null=True)
    peso_maquina_cuadriceps = models.IntegerField(null=True)
    peso_maquina_isquiotibiales = models.IntegerField(null=True)
    peso_gemelos = models.IntegerField(null=True)
    peso_biceps_mancuerna = models.IntegerField(null=True)
    peso_triceps_mancuerna = models.IntegerField(null=True)
    peso_elevaciones_laterales = models.IntegerField(null=True)
    peso_elevaciones_laterales_posterior = models.IntegerField(null=True)
    peso_press_militar = models.IntegerField(null=True)

class Clases(models.Model):
    horario = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    maquinas_disponibles = models.CharField(max_length=50)