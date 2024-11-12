from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Schedule
from .forms import RegistroEntradaForm, MetricasForm

def Index(request):
    return render(request, 'index.html')

def Membresias(request):
    return render(request, 'PortalMembresias.html')

def Login(request):
    return render(request, 'PortalLogin.html')

def Registro(request):
    return render(request, 'PortalRegistro.html')

def Clases_cliente(request):
    return render(request, 'clases_clientes.html')

def Clases_profesor(request):
    return render(request, 'clases_profesor.html')

def Metricas_clientes(request):
    form=MetricasForm()
    if request.method=='POST':
        form=MetricasForm(request.POST)
        if form.is_valid():
            form.save()
        return Index(request)
    data={'form':form,'titulo':'Agregar Medidas'}
    return render(request,'Metricas.html',data)


def Comunidad(request):
    return render(request, 'comunidad.html')

def Contactos(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        mensaje = request.POST.get('message')
        
        send_mail(
            f"Mensaje de {nombre}",
            mensaje,
            correo, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False,
        )
        return render(request, 'contacto.html', {'mensaje_enviado': True})
    return render(request, 'contacto.html')

def Inscripcion(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    return redirect('success_page') 

def RegistroEntrada(request):
    if request.method == 'POST':
        form = RegistroEntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = RegistroEntradaForm()
    
    return render(request, 'registro_entrada.html', {'form': form})