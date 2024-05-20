from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmarks.images'

    def ready(self):
        # import signal handlers
        import bookmarks.images.signals
