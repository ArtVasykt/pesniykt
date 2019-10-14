from django.apps import AppConfig


class PesniConfig(AppConfig):
    name = 'pesni'
    verbose_name = 'Песни (Игра)'

    def ready(self):
    	print('Готов прила')
    	from . import signals