from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegistroEntrada, MetricasCliente, MetricasTrenSuperior, MetricasTrenInferior,Clases, Membresias, Usuarios

class RegistroEntradaForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        label="RUT",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 12345678-9'})
    )

class MetricasClienteForm(forms.ModelForm):
    class Meta:
        model = MetricasCliente
        fields = [
            'altura', 
            'peso', 
            'horas_entrenadas',
        ]

class MetricasTrenSuperiorForm(forms.ModelForm):
    class Meta:
        model = MetricasTrenSuperior
        fields = [
            'peso_press_banca', 
            'peso_press_inclinado', 
            'peso_fondos', 
            'peso_jalon_al_pecho', 
            'peso_remo_polea', 
            'peso_remo_libre',
            'peso_dominada',
            'peso_biceps_mancuerna',
            'peso_triceps_mancuerna',
            'peso_elevaciones_laterales',
            'peso_elevaciones_laterales_posterior',
            'peso_press_militar',
        ]

class MetricasTrenInferiorForm(forms.ModelForm):
    class Meta:
        model = MetricasTrenInferior
        fields = [
            'peso_sentadilla_libre',
            'peso_sentadilla_bulgara',
            'peso_maquina_cuadriceps',
            'peso_maquina_isquiotibiales',
            'peso_gemelos',
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
    
class FormRegistro(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirmar Contraseña'}),
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Usuarios
        fields = ['username', 'email', 'telefono'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

                    
class MembresiasForm(forms.ModelForm):
    class Meta:
        model=Membresias
        fields= [
            'Nombre',
            'Precio',
            'Horario1',
            'Horario2',
        ]