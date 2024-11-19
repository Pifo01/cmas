from django import forms
from .models import RegistroEntrada, Metricas, Clases, Membresias

class RegistroEntradaForm(forms.ModelForm):
    class Meta:
        model = RegistroEntrada
        fields = ['nombre', 'rut', 'hora_entrada']

class MetricasForm(forms.ModelForm):
    class Meta:
        model = Metricas
        fields = [
            'altura', 
            'peso', 
            'peso_press_banca', 
            'peso_press_inclinado', 
            'peso_fondos', 
            'peso_jalon_al_pecho', 
            'peso_remo_polea', 
            'peso_remo_libre',
            'peso_dominada',
            'peso_sentadilla_libre',
            'peso_sentadilla_bulgara',
            'peso_maquina_cuadriceps',
            'peso_maquina_isquiotibiales',
            'peso_gemelos',
            'peso_biceps_mancuerna',
            'peso_triceps_mancuerna',
            'peso_elevaciones_laterales',
            'peso_elevaciones_laterales_posterior',
            'peso_press_militar',
        ]

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = [
            'Horario', 
            'Actividad', 
            'Maquinas_Diponibles',
        ]
                
class FormLogin(forms.Form):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu usuario',
            'required' : 'true'
        })
    )
    password= forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Ingresa tu contraseña',
            'required' : 'true'   
        })
    )

class MembresiasForm(forms.ModelForm):
    class Meta:
        model=Membresias
        fields= [
            'Nombre',
            'Precio',
            'Horario1',
            'Horario2',
        ]