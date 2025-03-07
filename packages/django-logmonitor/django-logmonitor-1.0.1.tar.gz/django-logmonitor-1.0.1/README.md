# Django LogMonitor <img src="URL_A_TU_LOGO" width="50" align="right">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/django-logmonitor.svg)](https://badge.fury.io/py/django-logmonitor)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Auditoría completa y sencilla para tus modelos Django.**

Django LogMonitor es una potente aplicación Django diseñada para simplificar la auditoría de las acciones de los usuarios en tus modelos. Con un enfoque en la facilidad de uso y la flexibilidad, LogMonitor te permite rastrear cada cambio, asegurando la integridad y la transparencia de tus datos.

## ✨ Características Destacadas

*   **Registro Exhaustivo:** Captura cada creación, actualización y eliminación de objetos en tus modelos.
*   **Riqueza de Detalles:** Almacena información crucial como el usuario responsable, la fecha y hora exactas, la dirección IP y el navegador utilizado.
*   **JSON para la Transparencia:** Visualiza los datos anteriores y nuevos en un formato JSON claro y fácil de interpretar.
*   **Control Total:** Excluye modelos y campos específicos de la auditoría para un enfoque personalizado.
*   **Panel de Administración Intuitivo:** Disfruta de una interfaz de administración personalizable que facilita la gestión y el análisis de los registros.
*   **Soporte Multilingüe:** Adapta la aplicación a tus necesidades lingüísticas con soporte para múltiples idiomas.
*   **Filtrado Avanzado:** Utiliza filtros dropdown en el panel de administración para una búsqueda y análisis eficientes de los datos.

## 🚀 Instalación

Instala Django LogMonitor con un simple comando:

```bash
pip install django-logmonitor

🛠️ Configuración

Añade la aplicación: Agrega 'logmonitor' a tu lista de INSTALLED_APPS en settings.py.

INSTALLED_APPS = [
    ...
    'logmonitor',
]

Activa el Middleware: Incluye logmonitor.middleware.RequestMiddleware en tu configuración de MIDDLEWARE.

MIDDLEWARE = [
    'logmonitor.middleware.RequestMiddleware',
    ...
]

(Opcional) Personaliza el AdminSite: Si utilizas un AdminSite personalizado, registra el modelo LogMonitor.

from logmonitor import register_logmonitor
from tu_proyecto.admin_site import admin_site  # Reemplaza con tu AdminSite

register_logmonitor(admin_site)

(Opcional) Excluye Modelos y Campos: Define qué modelos y campos excluir de la auditoría en settings.py.

LOGMONITOR_EXCLUDE_MODELS = ['app.Model', 'otra_app.OtroModel']
LOGMONITOR_EXCLUDE_FIELDS = ['fecha_modificacion', 'campo_interno']

⚙️ Dependencias

Asegúrate de tener instaladas las siguientes dependencias:

Django (>=3.2)

django-admin-list-filter-dropdown (>=1.0)

🤝 Contribución

¡Tu ayuda es bienvenida! Si encuentras errores, tienes sugerencias o quieres añadir nuevas características, no dudes en abrir un issue o enviar un pull request.

📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

Hecho con ❤️ por Javier L. Pulido