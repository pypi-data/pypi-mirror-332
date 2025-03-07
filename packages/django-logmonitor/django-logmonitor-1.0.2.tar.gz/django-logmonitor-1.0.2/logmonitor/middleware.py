from django.utils.translation import gettext_lazy as _

import threading

_requests = threading.local()

class RequestMiddleware:
    """Middleware para almacenar el request, usuario, IP y navegador en una variable de thread local."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _requests.request = request  # 🔥 Guardar request aquí
        
        # 🔥 Guardar usuario autenticado
        _requests.user = request.user if hasattr(request, 'user') and request.user.is_authenticated else None
        
        # 🔥 Guardar IP y navegador
        _requests.ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
        _requests.navegador = request.META.get('HTTP_USER_AGENT', _('Desconocido'))

        response = self.get_response(request)
        return response

def obtener_request():
    """Obtiene el request desde el almacenamiento del middleware."""
    return getattr(_requests, 'request', None)

def obtener_usuario_actual():
    """Obtiene el usuario desde el almacenamiento del middleware."""
    return getattr(_requests, 'user', None)

def obtener_ip():
    """Obtiene la IP desde el almacenamiento del middleware."""
    return getattr(_requests, 'ip', '0.0.0.0')

def obtener_navegador():
    """Obtiene el navegador desde el almacenamiento del middleware."""
    return getattr(_requests, 'navegador', _('Desconocido'))
