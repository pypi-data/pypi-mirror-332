def register_logmonitor(admin_site):

    from django.contrib import admin
    from .models import LogMonitor
    from .admin import LogMonitorAdmin

    admin_site.register(LogMonitor, LogMonitorAdmin)