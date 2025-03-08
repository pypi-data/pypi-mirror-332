from django.urls import path

from src.notifications.views import get_notifications

app_name = 'django_notifications'

urlpatterns = [
    path('admin/django_notifications/', get_notifications, name='django_notifications'),
]
