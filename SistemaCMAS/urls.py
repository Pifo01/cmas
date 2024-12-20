from django.urls import path

from PortalCMAS import views

urlpatterns = [
    path('', views.Index),
    path('Membresias/', views.MembresiasUsuarios),
    path('PortalLogin/', views.Login),
    path('PortalRegistro/', views.FormRegistro, name="PortalRegistro"),
    path('Clases_cliente/', views.Clases_cliente),
    path('Clases_profesor/', views.Clases_profesor),
    path('crear_clase/', views.Crear_Clase),
    path('ver_clase/<int:id>', views.Ver_Clase),
    path('actualizar_clase/<int:id>', views.Actualizar_Clase),
    path('eliminar_clase/<int:id>', views.Eliminar_Clase),
    path('progreso/', views.ProgresoCLiente),
    path('metricas_cliente/', views.Metricas_cliente),
    path('metricas_trensuperior/', views.Metricas_TrenSuperior),
    path('metricas_treninferior/', views.Metricas_TrenInferior),
    path('Comunidad/', views.Comunidad),
    path('Contactos/', views.Contactos),
    path('Inscripcion/', views.Inscripcion),
    path('RegistroEntrada/', views.RegistroEntrada),
    path('PortalAdmin/', views.Login_Admin),
    path('MembresiasAdmin/', views.MembresiasAdmin),
    path('crear_membresia/', views.CrearMembresias),
    path('eliminar_membresia/<int:id>', views.Eliminar_Membresia),
    path('actualizar_membresia/<int:id>', views.Actualizar_Membresia),
]
