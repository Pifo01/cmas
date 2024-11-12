Sistema de Gestión para Cmas GYM
Este proyecto es una página web desarrollada en Django que busca promover el gimnasio Cmas GYM, mostrando sus promociones y ofreciendo una plataforma de gestión de suscripciones. Los usuarios pueden crear una cuenta y acceder a planes de suscripción para aprovechar las instalaciones del gimnasio.

Descripción
La plataforma permite:

Explorar el gimnasio: Página principal con información del gimnasio y promociones.
Registro y autenticación: Los usuarios pueden crear cuentas, iniciar sesión y acceder a opciones de suscripción.
Gestión de suscripciones: Los usuarios registrados pueden suscribirse a los distintos planes ofrecidos por el gimnasio.
Requisitos
Python 3.12 (junto con el framework Django)
Django: Puedes instalarlo con pip install django.
MariaDB (con XAMPP para el entorno local)
XAMPP para la configuración de la base de datos de desarrollo local. En el futuro, el sistema planea migrar a una base de datos en la nube.
Instalación
Clonar el repositorio:

bash
Copiar código
git clone <url_del_repositorio>
cd <nombre_del_directorio>
Crear un entorno virtual (opcional pero recomendado):

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows, usa env\Scripts\activate
Instalar dependencias:

bash
Copiar código
pip install django
Configurar la base de datos en XAMPP:

Asegúrate de que MariaDB esté activo en XAMPP.
Crear una base de datos para el sistema.
Configurar las credenciales en el archivo settings.py de Django en la sección DATABASES.
Ejecutar migraciones para crear las tablas necesarias:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Iniciar el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Acceder a la aplicación en http://localhost:8000.

Comandos Principales
python manage.py runserver: Inicia el servidor de desarrollo.
python manage.py makemigrations: Detecta cambios en el modelo de datos.
python manage.py migrate: Aplica migraciones a la base de datos.
Autores
Sebastián Vargas
Ángel Rodríguez
Vicente Cumillaf
Matías Díaz