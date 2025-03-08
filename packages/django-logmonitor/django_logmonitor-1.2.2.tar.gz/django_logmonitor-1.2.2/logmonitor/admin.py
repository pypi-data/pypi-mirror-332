from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, escape
from .utils import truncar_texto
from django.urls import reverse
from django.apps import apps
import json
from django.conf import settings
from .models import LogMonitor
from django.db import models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.apps import apps

# Detectar si el proyecto usa admin.site o un admin personalizado
default_admin_site = admin.site  # Por defecto, usamos admin.site

for app_config in apps.get_app_configs():
    if hasattr(app_config.module, "admin_site"):
        default_admin_site = app_config.module.admin_site
        break  # Si encontramos un admin personalizado, lo usamos

class LogMonitorAdmin(admin.ModelAdmin):
    change_form_template = "admin/logmonitor/change_form.html"
    list_display = ('accion',  'fecha_hora', 'modelo_verbose_name', 'objeto_id', 'campos_editados', 'usuario')
    search_fields = ('usuario__username', 'objeto_id', 'ip', 'navegador', 'dato_anterior', 'dato_nuevo', 'app_label', 'model_name', 'accion')
    readonly_fields = ('usuario', 'fecha_hora', 'accion', 'objeto_id', 'dato_anterior_formateado', 'dato_nuevo_formateado', 'ip', 'navegador', 'dato_anterior_json', 'dato_nuevo_json', 'app_label', 'model_name')
    ordering = ('-fecha_hora',)
    list_per_page = 20
    date_hierarchy = 'fecha_hora'
    #actions = None


    list_filter = (
        ('app_label', DropdownFilter),
        ('model_name', DropdownFilter),
        ('accion', ChoiceDropdownFilter),
    )

    fieldsets = (
        (_('Detalles de la acción'), {
            'fields': (('accion', 'fecha_hora'), ('app_label', 'model_name', 'objeto_id',),),
            'classes': ('wide'),
        }),
        (None, {
            'fields': ('dato_anterior_formateado', 'dato_nuevo_formateado',),
            #'classes': ('extrapretty',),  # Colapsar este fieldset por defecto
        }),
        (_('Información del usuario'), {
            'fields': ('usuario', 'ip', 'navegador',),
        }),
        (_('Datos en formato JSON'), {
            'fields': (('dato_anterior_json', 'dato_nuevo_json')),
            'classes': ('extrapretty', 'collapse',),  # Colapsar este fieldset por defecto
        }),

    )

    def campos_editados(self, obj):
        """Muestra los campos editados con sus valores anteriores y nuevos, usando valores de choice."""
        if obj.accion == 'create':

            # En caso de creación, mostrar "Nuevo registro" como enlace al detalle del registro
            admin_namespace = default_admin_site.name  # Detectar namespace correcto
            url = reverse(f'{admin_namespace}:logmonitor_logmonitor_change', args=[obj.id])
            #url = reverse('custom_admin:logmonitor_logmonitor_change', args=[obj.id])

            return format_html("<a href='{}'>{}</a>", url, _("Nuevo registro"))

        
        elif obj.accion == 'delete':

            # En caso de eliminación, mostrar "Registro eliminado" como enlace al detalle del registro
            admin_namespace = default_admin_site.name  # Detectar namespace correcto
            url = reverse(f'{admin_namespace}:logmonitor_logmonitor_change', args=[obj.id])
            #url = reverse('custom_admin:logmonitor_logmonitor_change', args=[obj.id])

            return format_html("<a href='{}'>{}</a>", url, _('Registro eliminado'))
        
        elif obj.dato_anterior and obj.dato_nuevo:
            # En caso de actualización, mostrar los campos editados
            campos_editados = []
            
            # Obtener el modelo original
            try:
                modelo_original = apps.get_model(obj.app_label, obj.model_name)
            except LookupError:
                modelo_original = None

            # Verificar si hay cambios en campos no excluidos
            hay_cambios = False

            for campo, valor_nuevo in obj.dato_nuevo.items():
                if campo in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
                    continue  # Saltar campos excluidos

                valor_anterior = obj.dato_anterior.get(campo, None)
                if valor_anterior != valor_nuevo:
                    hay_cambios = True  # Hay cambios en campos no excluidos

                    # Obtener el verbose_name del campo
                    campo_nombre = campo
                    if modelo_original:
                        try:
                            field = modelo_original._meta.get_field(campo)
                            campo_nombre = field.verbose_name if field.verbose_name else campo
                        except:
                            pass  # Si no se puede obtener el campo, usar el nombre original

                    # Obtener el valor de choice si el campo es un campo choice
                    if modelo_original:
                        try:
                            field = modelo_original._meta.get_field(campo)
                            if field.choices:
                                valor_anterior = dict(field.choices).get(valor_anterior, valor_anterior)
                                valor_nuevo = dict(field.choices).get(valor_nuevo, valor_nuevo)
                        except:
                            pass  # Si no es un campo choice, continuar sin cambios

                    # Cortar valores largos y agregar puntos suspensivos
                    valor_anterior = truncar_texto(str(valor_anterior))  # Llamada a la función independiente
                    valor_nuevo = truncar_texto(str(valor_nuevo))  # Llamada a la función independiente

                    # Mostrar el campo y los valores editados
                    campos_editados.append(
                        f"<b>{campo_nombre}:</b><br>"
                        f"<span style='font-style: italic;'>{valor_anterior}</span> "
                        f"<span style='font-weight:bold; font-size: 1.2em; color: #40b313;'>→</span> "
                        f"<span>{valor_nuevo}</span>"
                    )

            if not hay_cambios:
                # Si no hay cambios en campos no excluidos, mostrar un mensaje
                return _("No se hicieron modificaciones")

            return format_html("<br>".join(campos_editados))
        return _('No disponible')
    campos_editados.short_description = _('Detalles de la acción')

    def modelo_verbose_name(self, obj):
        """Muestra el verbose_name del modelo."""
        try:
            modelo_original = apps.get_model(obj.app_label, obj.model_name)
            return modelo_original._meta.verbose_name
        except LookupError:
            return obj.model_name  # Si no se puede obtener el verbose_name, mostrar el nombre del modelo
    modelo_verbose_name.short_description = _('Modelo')

    def dato_anterior_formateado(self, obj):
        if obj.accion == 'create':
            return _('Es un registro nuevo ó los datos no estan disponibles.')  # No mostrar nada para creaciones
        elif obj.dato_anterior:
            # Obtener el modelo original
            try:
                modelo_original = apps.get_model(obj.app_label, obj.model_name)
            except LookupError:
                modelo_original = None

            # Formatear los datos anteriores
            datos_formateados = []
            for campo, valor in obj.dato_anterior.items():
                if campo in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
                    continue  # Saltar campos excluidos

                # Obtener el verbose_name del campo
                campo_nombre = campo
                if modelo_original:
                    try:
                        field = modelo_original._meta.get_field(campo)
                        campo_nombre = field.verbose_name if field.verbose_name else campo
                    except:
                        pass  # Si no se puede obtener el campo, usar el nombre original

                # Obtener el valor de choice si el campo es un campo choice
                if modelo_original:
                    try:
                        field = modelo_original._meta.get_field(campo)
                        if field.choices:
                            valor = dict(field.choices).get(valor, valor)
                    except:
                        pass  # Si no es un campo choice, continuar sin cambios

                # Agregar el campo y el valor formateado
                datos_formateados.append(f"<b>{campo_nombre}:</b> {valor}")
            return format_html("<br>".join(datos_formateados))
        return _('No disponible')
    dato_anterior_formateado.short_description = _('DATOS ANTERIORES')

    def dato_nuevo_formateado(self, obj):
        if obj.accion == 'create':
            # Mostrar todos los campos para creaciones
            try:
                modelo_original = apps.get_model(obj.app_label, obj.model_name)
            except LookupError:
                modelo_original = None

            # Formatear los datos nuevos
            datos_formateados = []
            for campo, valor in obj.dato_nuevo.items():
                if campo in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
                    continue  # Saltar campos excluidos

                # Obtener el verbose_name del campo
                campo_nombre = campo
                if modelo_original:
                    try:
                        field = modelo_original._meta.get_field(campo)
                        campo_nombre = field.verbose_name if field.verbose_name else campo
                    except:
                        pass  # Si no se puede obtener el campo, usar el nombre original

                # Obtener el valor de choice si el campo es un campo choice
                if modelo_original:
                    try:
                        field = modelo_original._meta.get_field(campo)
                        if field.choices:
                            valor = dict(field.choices).get(valor, valor)
                    except:
                        pass  # Si no es un campo choice, continuar sin cambios

                # Agregar el campo y el valor formateado
                datos_formateados.append(f"<b>{campo_nombre}:</b> {valor}")
            return format_html("<br>".join(datos_formateados))
        elif obj.accion == 'delete':
            return _('Registro eliminado')  # Mensaje para eliminaciones
        elif obj.dato_anterior and obj.dato_nuevo:
            # Pasar solo los campos editados
            try:
                modelo_original = apps.get_model(obj.app_label, obj.model_name)
            except LookupError:
                modelo_original = None

            # Formatear los datos nuevos
            datos_formateados = []
            for campo, valor in obj.dato_nuevo.items():
                if campo in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
                    continue  # Saltar campos excluidos

                # Solo mostrar campos editados
                if obj.dato_anterior.get(campo) != valor:
                    # Obtener el verbose_name del campo
                    campo_nombre = campo
                    if modelo_original:
                        try:
                            field = modelo_original._meta.get_field(campo)
                            campo_nombre = field.verbose_name if field.verbose_name else campo
                        except:
                            pass  # Si no se puede obtener el campo, usar el nombre original

                    # Obtener el valor de choice si el campo es un campo choice
                    if modelo_original:
                        try:
                            field = modelo_original._meta.get_field(campo)
                            if field.choices:
                                valor = dict(field.choices).get(valor, valor)
                        except:
                            pass  # Si no es un campo choice, continuar sin cambios

                    # Agregar el campo y el valor formateado
                    datos_formateados.append(f"<b>{campo_nombre}:</b> {valor}")
            return format_html("<br>".join(datos_formateados))
        return _('No disponible')
    dato_nuevo_formateado.short_description = _('DATOS NUEVOS')



    def dato_anterior_json(self, obj):
        if obj.dato_anterior:
            json_data = json.dumps(obj.dato_anterior, indent=2, ensure_ascii=False)
            return format_html(
                '<pre id="dato_anterior_json">{}</pre>'
                '<button type="button" class="button" onclick="copiarJSON(event, \'dato_anterior_json\')">{}</button>',
                json_data,
                _("Copiar")
            )
        return _('Es un registro nuevo ó los datos no estan disponibles.')

    dato_anterior_json.short_description = _('DATOS ANTERIORES (json)')

    def dato_nuevo_json(self, obj):
        if obj.dato_nuevo:
            json_data = json.dumps(obj.dato_nuevo, indent=2, ensure_ascii=False)
            return format_html(
                '<pre id="dato_nuevo_json">{}</pre>'
                '<button type="button" class="button" onclick="copiarJSON(event, \'dato_nuevo_json\')">{}</button>',
                json_data,
                _("Copiar")
            )
        return _('Es un registro nuevo ó los datos no estan disponibles.')

    dato_nuevo_json.short_description = _('DATOS NUEVOS (json)')

    def _formatear_datos(self, datos, titulo):
        """Formatea los datos para que sean más fáciles de entender, usando valores de choice."""
        html = f"<div>"
        for campo, valor in datos.items():
            # Excluir campos definidos en LOGMONITOR_EXCLUDE_FIELDS
            if campo in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
                continue  # Saltar este campo

            # Obtener el valor de choice si el campo es un campo choice
            try:
                field = self.model._meta.get_field(campo)
                if field.choices:
                    valor = dict(field.choices).get(valor, valor)
            except:
                pass  # Si no es un campo choice, continuar sin cambios

            # Si es un ForeignKey, obtener el ID del objeto relacionado
            try:
                field = self.model._meta.get_field(campo)
                if isinstance(field, models.ForeignKey):
                   pass # Eliminar las líneas redundantes
            except:
                pass

            # Escapar el valor para evitar problemas con caracteres especiales
            valor_escapado = escape(str(valor))
            html += f"<p><strong>{campo}:</strong> {valor_escapado}</p>"
        html += "</div>"
        return format_html(html)

    class Media:
        js = ('logmonitor/js/copiar_json.js',)

    def has_add_permission(self, request):
        return False
