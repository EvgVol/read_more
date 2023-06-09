from django.apps import AppConfig


class VookmarksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vookmarks'
    verbose_name = 'Визуальные закладки'

    def ready(self):
        import vookmarks.signals