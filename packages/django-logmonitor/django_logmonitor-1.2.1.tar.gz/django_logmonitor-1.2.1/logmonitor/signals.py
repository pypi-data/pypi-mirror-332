from django.conf import settings
from django.db.models.signals import pre_save, post_save, post_delete
from django.db.migrations.recorder import MigrationRecorder
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from .models import LogMonitor
from decimal import Decimal
import json
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import logging
import threading
from logmonitor.middleware import obtener_usuario_actual, obtener_ip, obtener_navegador


logger = logging.getLogger(__name__)

User = get_user_model()

_requests = threading.local()


# Lista de modelos excluidos por defecto (puedes agregar más si es necesario)
MODELOS_EXCLUIDOS_POR_DEFECTO = [LogMonitor, Session, LogEntry, MigrationRecorder.Migration,]

# Diccionario para almacenar los valores anteriores de los objetos
valores_anteriores = {}


def obtener_request():
    """Obtiene el request desde un almacenamiento seguro en hilos."""
    return getattr(_requests, 'request', None)



def convertir_a_serializable(valor):
    """Convierte valores complejos a un formato serializable."""
    if isinstance(valor, datetime):
        return valor.isoformat()
    if isinstance(valor, Decimal):
        return str(valor)  # 🔥 Guardar como string para evitar pérdida de precisión
    if isinstance(valor, (User, ContentType)):
        return valor.pk
    if isinstance(valor, models.FileField):
        return valor.name if valor else None
    if isinstance(valor, models.Model):
        return valor.pk if hasattr(valor, 'pk') else str(valor)
    if isinstance(valor, models.Manager):  # 🔥 Manejar ManyToManyFields correctamente
        return list(valor.values_list('pk', flat=True))
    if isinstance(valor, list):
        return [convertir_a_serializable(v) for v in valor]
    if isinstance(valor, dict):
        return {k: convertir_a_serializable(v) for k, v in valor.items()}
    if isinstance(valor, (str, int, float, bool)) or valor is None:
        return valor
    return str(valor)  # Última opción: convertir a string

def obtener_campos_excluidos(sender):
    """Obtiene los campos que tienen auto_now_add=True o están en LOGMONITOR_EXCLUDE_FIELDS."""
    campos_excluidos = []
    for field in sender._meta.fields:
        # Excluir campos con auto_now_add=True o auto_now=True
        if getattr(field, 'auto_now_add', False) or getattr(field, 'auto_now', False):
            campos_excluidos.append(field.name)
        # Excluir campos definidos en LOGMONITOR_EXCLUDE_FIELDS
        if field.name in getattr(settings, 'LOGMONITOR_EXCLUDE_FIELDS', []):
            campos_excluidos.append(field.name)
    return campos_excluidos

def obtener_modelos_excluidos():
    """Obtiene la lista de modelos excluidos de la auditoría."""
    modelos_excluidos = MODELOS_EXCLUIDOS_POR_DEFECTO.copy()

    # Agregar modelos excluidos definidos en settings.py
    for model_path in getattr(settings, 'LOGMONITOR_EXCLUDE_MODELS', []):
        try:
            app_label, model_name = model_path.split('.')
            model = apps.get_model(app_label, model_name)
            if model:
                modelos_excluidos.append(model)
        except Exception:
            pass

    return modelos_excluidos

MODELOS_EXCLUIDOS = obtener_modelos_excluidos()

@receiver(pre_save)
def pre_save_handler(sender, instance, **kwargs):
    if sender in MODELOS_EXCLUIDOS:
        return  # No auditar modelos excluidos

    campos_excluidos = obtener_campos_excluidos(sender)

    if instance.pk:  # Si el objeto ya existe (es una actualización)
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            valores_anteriores[instance.pk] = {
                field.name: getattr(old_instance, field.name)
                for field in old_instance._meta.fields
                if field.name not in campos_excluidos
            }

            # Manejar campos ManyToMany
            for field in old_instance._meta.many_to_many:
                if field.name not in campos_excluidos:
                    valores_anteriores[instance.pk][field.name] = list(getattr(old_instance, field.name).values_list('pk', flat=True))
        except sender.DoesNotExist:
            valores_anteriores[instance.pk] = None
    else:
        valores_anteriores[instance.pk] = None  # Es una creación, no hay valor anterior

@receiver(post_save)
def registrar_creacion_actualizacion(sender, instance, created, **kwargs):
    """Registra la creación o actualización de un objeto en el LogMonitor."""
    if sender in MODELOS_EXCLUIDOS:
        return  # No auditar modelos excluidos

    request = obtener_request()
    usuario = obtener_usuario_actual()
    navegador = obtener_navegador()  # 🔥 Ahora se obtiene desde el Middleware
    ip = obtener_ip()  # 🔥 Ahora se obtiene desde el Middleware

    campos_excluidos = obtener_campos_excluidos(sender)

    if not created:
        dato_anterior = valores_anteriores.get(instance.pk, None)
        if dato_anterior is None:
            return

        dato_nuevo = {
            field.name: convertir_a_serializable(getattr(instance, field.name))
            for field in instance._meta.fields
            if field.name not in campos_excluidos
        }

        if dato_anterior == dato_nuevo:
            return

        dato_anterior = {
            field: convertir_a_serializable(valor)
            for field, valor in dato_anterior.items()
        }

        if instance.pk in valores_anteriores:
            del valores_anteriores[instance.pk]

    else:  # Si es una creación
        dato_anterior = None
        dato_nuevo = {
            field.name: convertir_a_serializable(getattr(instance, field.name))
            for field in instance._meta.fields
            if field.name not in campos_excluidos
        }

    LogMonitor.objects.create(
        usuario=usuario,
        accion=LogMonitor.ACTION_CREATE if created else LogMonitor.ACTION_UPDATE,
        app_label=sender._meta.app_label,
        model_name=sender._meta.model_name,
        objeto_id=str(instance.pk),
        dato_anterior=dato_anterior,
        dato_nuevo=dato_nuevo,
        navegador=navegador,
        ip=ip,
    )


@receiver(post_delete)
def registrar_eliminacion(sender, instance, **kwargs):
    """Registra la eliminación de un objeto en el LogMonitor."""
    if sender in MODELOS_EXCLUIDOS:
        return  # No auditar modelos excluidos

    request = obtener_request()
    usuario = obtener_usuario_actual()
    navegador = obtener_navegador()  # 🔥 Ahora se obtiene desde el Middleware
    ip = obtener_ip()  # 🔥 Ahora se obtiene desde el Middleware

    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    objeto_id = str(instance.pk)

    # Guardar el estado del objeto antes de eliminarlo
    dato_anterior = {
        field.name: convertir_a_serializable(getattr(instance, field.name))
        for field in instance._meta.fields
    }

    LogMonitor.objects.create(
        usuario=usuario,
        accion=LogMonitor.ACTION_DELETE,
        app_label=app_label,
        model_name=model_name,
        objeto_id=objeto_id,
        dato_anterior=dato_anterior,
        dato_nuevo=None,
        navegador=navegador,
        ip=ip,
    )
