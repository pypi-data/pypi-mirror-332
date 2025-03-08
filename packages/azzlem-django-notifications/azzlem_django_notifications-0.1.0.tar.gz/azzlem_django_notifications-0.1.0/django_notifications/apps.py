from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.django_notifications"

    def ready(self):
        import src.notifications.signals
