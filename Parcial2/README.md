# Mi Proyecto de Lista de Tareas en Flask

Este es un proyecto simple de una aplicación web en Flask que permite gestionar una lista de tareas. A lo largo de este taller, prestamos especial atención a la estructura del proyecto y a las buenas prácticas de desarrollo.

## Requisitos Previos

- Python 3.x
- Dependencias listadas en `requirements.txt`
- Base de datos Microsoft Access (configurada según `config.py`)

## Configuración

Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno local:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/
   cd mi-proyecto-flask

## 1 Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Windows, usa venv\Scripts\activate

## 2 Instala las dependencias:
pip install -r requirements.txt

## 3 Configura las variables de entorno (opcional):
Crea un archivo .env en el directorio raíz y define las variables de entorno según sea necesario.

## 4 Configura la base de datos:
Asegúrate de tener una base de datos Microsoft Access configurada y actualiza la cadena de conexión en config.py según sea necesario.

## 5 Ejecuta la aplicación:
python wsgi.py
Accede a la aplicación en tu navegador web: http://localhost:5000

## 6 Uso
Visita la página principal para ver todas las tareas.
Agrega nuevas tareas desde la página de agregar tarea.
Elimina tareas haciendo clic en el enlace "Eliminar".

## 7 Estructura del Proyecto
/Parcial 2/
|-- /app/
| |-- /templates/
| |-- /static/
| |-- /blueprints/
| |-- /models/
| |-- __init__.py
| |-- config.py
| |-- extensions.py
|
|-- /migrations/
|-- database.accdb
|-- .gitignore
|-- requirements.txt
|-- wsgi.py
|-- README.md






