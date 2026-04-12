# API Taller 2 - Evaluación 2 (Grupo 7)

Este repositorio contiene la estructura base y la conexión a la base de datos PostgreSQL para nuestro proyecto.

## 🚀 Avances y Estructura Base

Hasta el momento, se han configurado los pilares del proyecto:

* **Conexión a la Base de Datos (`db/database.py`)**: Configuración del motor de SQLAlchemy y gestión de sesiones conectadas al servidor del profesor.
* **Modelos de Datos (`models/models.py`)**: Creación de las tablas `Personal` y `Formacion`, mapeadas correctamente al esquema asignado (`grupo_7`).
* **Seguridad de Credenciales**: Se separó la cadena de conexión usando variables de entorno (`.env`) para no exponer contraseñas en el repositorio público.

---

## 🛠️ Configuración de la Base de Datos (MUY IMPORTANTE)

Por motivos de seguridad y buenas prácticas, la contraseña real y la dirección de la base de datos **NO están subidas a GitHub**. Para que el proyecto les funcione localmente, deben seguir estos pasos:

1. **Localizar la plantilla**: En la raíz del proyecto verán un archivo llamado `.env.example`.
2. **Crear su archivo local**: Creen un nuevo archivo en la raíz llamado exactamente **`.env`** (asegúrense de incluir el punto al principio).
3. **Copiar contenido**: Copien todo lo que hay dentro de `.env.example` y péguenlo en su nuevo archivo `.env`.
4. **Solicitar credenciales**: la contraseña real de la base de datos se encuentra en las instrucciones de teams que el profe nos dejo y reemplácenla en el archivo donde dice `usuario_aqui:contraseña_aqui`.

> **Nota:** El archivo `.env` está en el `.gitignore`, por lo que nunca se subirá al repositorio compartido. Cada integrante debe tener su propio archivo local.

---

## 🛠️ Instrucciones para el Equipo (Cómo arrancar)

Para que el proyecto les funcione en sus computadoras locales sin errores de base de datos, sigan estos pasos una vez hagan el `git clone` o `git pull`:


### Como iniciar la app
La app se inicia con el comando:

 uvicorn main:app --reload

### 1. Activar entorno virtual e instalar dependencias
Asegúrense de tener el entorno virtual activo y ejecuten:
```bash
pip install -r requirements.txt

