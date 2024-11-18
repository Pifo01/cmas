from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from .models import Schedule
from PortalCMAS.models import Clases
from .forms import RegistroEntradaForm, MetricasForm, ClasesForm, FormLogin

def Index(request):
    return render(request, 'index.html')

def Membresias(request):
    return render(request, 'PortalMembresias.html')

def Login(request):
    form = FormLogin(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('PortalUsuario')
        else:
            messages.error(request,"Usuario o Contraseña incorrectos.")
    return render(request, 'PortalLogin.html', {'form': form})

def Registro(request):
    return render(request, 'PortalRegistro.html')

def Clases_cliente(request):
    clases=Clases.objects.all()
    data={'clases':clases}
    return render(request, 'clases_clientes.html',data)

def Clases_profesor(request):
    clases=Clases.objects.all()
    data={'clases':clases}
    return render(request, 'clases_profesor.html',data)

def Crear_Clase(request):
    form=ClasesForm()
    if request.method=='POST':
        form=ClasesForm(request.POST)
        if form.is_valid():
            form.save()
        return Clases_profesor(request)
    data={'form':form,'titulo':'Agregar Clases'}
    return render(request,'clases_save.html',data)

def Ver_Clase(request,id):
    clases=Clases.objects.get(id=id)
    data={"clases":clases}
    return render(request,'clases_ver.html',data)

def Actualizar_Clase(request,id):
    clases=Clases.objects.get(id=id)
    form=ClasesForm(instance=clases)
    if request.method=="POST":
        form=ClasesForm(request.POST,instance=clases)
        if form.is_valid():
            form.save()
        return Clases_profesor(request)
    data={'form':form,'titulo':'Actualizar Clase'}
    return render(request,'clases_save.html',data)


def Eliminar_Clase(request, id):
    try:
        clases = Clases.objects.get(id=id)
    except Clases.DoesNotExist:
        return redirect('../Clases_profesor/')

    if request.method == 'POST':
        clases.delete()
        return redirect('../Clases_profesor/')
    
    return render(request, 'clases_eliminar.html', {'clases': clases})

def Login_Admin(request):
    return render(request, 'PortalAdministrativo.html')

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