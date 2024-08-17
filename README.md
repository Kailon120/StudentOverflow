# StudentOverflow

StudentOverflow es un proyecto para el entrenamiento como desarrollador, utilizando Django.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes paqueterías:

### Paqueterías de Python
- asgiref==3.8.1
- Django==5.1
- psycopg2-binary==2.9.9
- sqlparse==0.5.1

## Configuración del Proyecto

- 1. Clona el repositorio:
     
     ```bash
     git clone https://github.com/tu_usuario/studentoverflow.git

- 2. Navega a la carpeta del repositorio:

     ```bash
     cd studentoverflow
     ```
 
- 3. Configura el entorno virtual y las dependencias:

     Crea un entorno virtual:
       ```bash
       python -m venv venv
       ```
     Activa el entorno virtual:
     
       En Windows:
       
       ```bash
       venv\Scripts\activate
       ```

       En macOS y Linux:
       
       ```bash
       source venv/bin/activate
       ```

     Instala las dependencias:
     
     ```bash
     pip install -r requirements.txt
     ```
     
- 4. Ejecuta las migraciones y arranca el servidor:

     Ejecuta las migraciones:
       ```bash
       python manage.py migrate
       ```

     Arranca el servidor de desarrollo:
       ```bash
       python manage.py runserver
       ```

## Nota

Recuerda configurar tu base de datos, en este proyecto se usó postgres:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myapp',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Así como también configurar el archivo settings.
