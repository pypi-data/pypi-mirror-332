from django.apps import AppConfig

class LogMonitorConfig(AppConfig):
    name = 'logmonitor'
    verbose_name = 'LogMonitor'

    def ready(self):
        # Importar las señales
        import logmonitor.signals  # Para registrar las señales