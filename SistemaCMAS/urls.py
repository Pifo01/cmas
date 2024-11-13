from django.urls import path
from PortalCMAS.views import Index, Membresias, Login, Registro, Clases_cliente, Clases_profesor, Comunidad, Contactos, Inscripcion, RegistroEntrada, Metricas_clientes, Login_Admin

urlpatterns = [
    path('', Index),
    path('Membresias/', Membresias),
    path('PortalLogin/', Login),
    path('PortalRegistro/', Registro),
    path('Clases_cliente/', Clases_cliente),
    path('Clases_profesor/', Clases_profesor),
    path('Progreso/', Metricas_clientes),
    path('Comunidad/', Comunidad),
    path('Contactos/', Contactos),
    path('Inscripcion/', Inscripcion),
    path('RegistroEntrada/', RegistroEntrada),
    path('PortalAdmin/', Login_Admin)
]
