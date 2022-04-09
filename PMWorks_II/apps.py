from django.apps import AppConfig
from django.conf import settings


class PmworksIiConfig(AppConfig):
    name = 'PMWorks_II'

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()
