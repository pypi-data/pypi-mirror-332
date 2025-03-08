from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class LogMonitor(models.Model):
    ACTION_CREATE = 'create'
    ACTION_UPDATE = 'update'
    ACTION_DELETE = 'delete'
    ACTION_CHOICES = [
        (ACTION_CREATE, _('Creación')),
        (ACTION_UPDATE, _('Actualización')),
        (ACTION_DELETE, _('Eliminación')),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Usuario'))
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha y Hora'))
    accion = models.CharField(max_length=10, choices=ACTION_CHOICES, verbose_name=_('Acción'))
    app_label = models.CharField(max_length=255, verbose_name=_('App'))  # Nombre de la aplicación
    model_name = models.CharField(max_length=255, verbose_name=_('Modelo'))  # Nombre del modelo
    objeto_id = models.CharField(max_length=255, verbose_name=_('ID del Objeto'))  # Ahora es un CharField para soportar UUID, etc.
    dato_anterior = models.JSONField(blank=True, null=True, verbose_name=_('Dato Anterior'))  # Datos anteriores
    dato_nuevo = models.JSONField(blank=True, null=True, verbose_name=_('Dato Nuevo'))  # Datos nuevos
    navegador = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Navegador'), default=_('Desconocido'))  # Navegador del usuario
    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name=_('Dirección IP'))  # IP del usuario

    class Meta:
        verbose_name = _('Registro de Auditoría')
        verbose_name_plural = _('Registros de Auditoría')
        ordering = ['-fecha_hora']

    def save(self, *args, **kwargs):
        # Evitar la recursividad al crear registros de LogMonitor
        if self._state.adding:
            super().save(*args, **kwargs)
        else:
            # No permitir actualizaciones en LogMonitor
            return

    def __str__(self):
        return f'{_(self.get_accion_display())} - {self.app_label}.{self.model_name} ({self.objeto_id}) | {self.usuario}'