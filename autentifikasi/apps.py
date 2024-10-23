from django.apps import AppConfig


class autentifikasi(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autentifikasi'
    def ready(self):
        import autentifikasi.signals