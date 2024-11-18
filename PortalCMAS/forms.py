from django import forms
from .models import RegistroEntrada, Metricas, Clases

class RegistroEntradaForm(forms.ModelForm):
    class Meta:
        model = RegistroEntrada
        fields = ['nombre', 'rut', 'hora_entrada']

class MetricasForm(forms.ModelForm):
    class Meta:
        model=Metricas
        fields = [
            'Altura', 
            'Peso', 
            'Peso_press_banca', 
            'Peso_press_inclinado', 
            'Peso_fondos', 
            'Peso_jalon_al_pecho', 
            'Peso_remo_polea', 
            'Peso_remo_libre',
            'Peso_dominada',
            'Peso_sentadilla_libre',
            'Peso_sentadilla_bulgara',
            'Peso_maquina_cuadriceps',
            'Peso_maquina_isquiotibiales',
            'Peso_gemelos',
            'Peso_biceps_mancuerna',
            'Peso_triceps_mancuerna',
            'Peso_elevaciones_laterales',
            'Peso_elevaciones_laterales_posterior',
            'Peso_press_militar',
        ]

class ClasesForm(forms.ModelForm):
    class Meta:
        model=Clases
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