from django.apps import apps
from django.utils.translation import gettext_lazy as _


def truncar_texto(texto, max_length=50):
    """Corta el texto y agrega puntos suspensivos si es demasiado largo."""
    if texto and len(texto) > max_length:
        return f"{texto[:max_length]}..."
    return texto

