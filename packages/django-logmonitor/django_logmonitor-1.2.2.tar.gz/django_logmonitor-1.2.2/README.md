
# LogMonitor <!--<img src="LOGO" width="50" align="right">-->

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/django-logmonitor.svg?cacheSeconds=3600)](https://pypi.org/project/django-logmonitor/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/JaviPulido/LogMonitor/graphs/commit-activity)

**Auditoría completa y sencilla para tus modelos Django.**

LogMonitor es una potente aplicación Django diseñada para simplificar la auditoría de las acciones de los usuarios en tus modelos. Con un enfoque en la facilidad de uso y la flexibilidad, LogMonitor te permite rastrear cada cambio, asegurando la integridad y la transparencia de tus datos.

## ✨ Características Destacadas

*   **Registro Exhaustivo:** Captura cada creación, actualización y eliminación de objetos en tus modelos.
*   **Información Detallada:** Almacena información crucial como el usuario responsable, la fecha y hora exactas, la dirección IP y el navegador utilizado.
*   **Visualización JSON:** Muestra los datos anteriores y nuevos en un formato JSON claro y fácil de interpretar, opción "Copiar JSON" para exportaciones de datos.
*   **Flexibilidad:** Permite excluir modelos y campos específicos de la auditoría para un enfoque personalizado.
*   **Panel de Administración Intuitivo:** Disfruta de una interfaz de administración personalizable que facilita la gestión y el análisis de los registros.
*   **Soporte Multilingüe:** Adapta la aplicación a tus necesidades lingüísticas con soporte para múltiples idiomas.
*   **Filtrado Avanzado:** Utiliza filtros dropdown en el panel de administración para una búsqueda y análisis eficientes de los datos.

## 🚀 Instalación

Instala LogMonitor con un simple comando:

```bash
pip install django-logmonitor
```

## 🛠️ Configuración en solo 3 pasos
1. **Añade la aplicación:** Agrega 'logmonitor' a tu lista de INSTALLED_APPS en `settings.py`.  

```python
INSTALLED_APPS = [
    ...
    'logmonitor',
]
```

2. **Activa el Middleware:** Incluye logmonitor.middleware.RequestMiddleware en tu configuración de MIDDLEWARE.
```python
MIDDLEWARE = [
    'logmonitor.middleware.RequestMiddleware',
    ...
]
```

3. **Migraciones:** Genera y aplica las migraciones necesarias para actualizar la base de datos con los cambios recientes en los modelos
```bash
python manage.py makemigrations logmonitor
python manage.py migrate logmonitor
```

### _(Opcional)_ Personaliza el AdminSite: Solo si utilizas un AdminSite personalizado (ej. admin_site), registra el modelo LogMonitor.
```python
from logmonitor import register_logmonitor
from tu_proyecto.admin_site import admin_site  # Reemplaza con tu AdminSite

register_logmonitor(admin_site)
```

### _(Opcional)_ Excluye Modelos y Campos: Define qué modelos y campos excluir de la auditoría en `settings.py`.
```python
LOGMONITOR_EXCLUDE_MODELS = ['app.Model', 'otra_app.OtroModel']
LOGMONITOR_EXCLUDE_FIELDS = ['fecha_modificacion', 'campo_interno']
```

 #### **NOTA:** **_Por defecto LogMonitor excluye los modelos: Session, LogEntry, MigrationRecorder.Migration; esto para evitar:_**

* **Registros de auditoría redundantes:** El modelo Session registra información sobre las sesiones de los usuarios, y el modelo LogEntry registra las acciones realizadas en el panel de administración de Django. Auditar estos modelos podría generar una gran cantidad de registros irrelevantes y dificultar la búsqueda de información importante.

* **Problemas de recursión:** Auditar el modelo LogEntry podría generar un bucle infinito, ya que cada vez que se crea un registro en LogEntry, se activaría la señal post_save, lo que generaría otro registro en LogEntry, y así sucesivamente.

* **Información técnica irrelevante para la mayoría de los usuarios:** El modelo MigrationRecorder.Migration registra información sobre las migraciones de la base de datos, que es información técnica que no es relevante para la mayoría de los usuarios.

## ⚙️ Dependencias

Asegúrate de tener instaladas:

*   Django (>=3.2)

* [django-admin-list-filter-dropdown](https://github.com/mrts/django-admin-list-filter-dropdown) (>=1.0): _Proporcionada por [Mart Sõmermaa](https://github.com/mrts)_.  Esta librería facilita la creación de filtros dropdown en el panel de administración de Django, y LogMonitor la incluye para mejorar la experiencia de usuario al filtrar los registros de auditoría.
**LogMonitor gestiona esta librería internamente, por lo que no es necesario añadirla a tu `INSTALLED_APPS` a menos que la estés utilizando directamente en otras partes de tu proyecto.**

## 🤝 Contribución
¡Tu ayuda es bienvenida! Si encuentras errores, tienes sugerencias o quieres añadir nuevas características, no dudes en abrir un issue o enviar un pull request.

## 📄 Licencia
Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

Hecho con ❤️ por [Javier L. Pulido](https://github.com/JaviPulido/LogMonitor)