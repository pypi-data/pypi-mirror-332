from django.db.models.signals import post_save
from django.dispatch import receiver


from src.feedback.models import Feedback
from src.notifications.models import Notification
from src.team.models import TeamModel


TRACKED_MODELS = [Feedback, TeamModel]

def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            app_name_model=instance._meta.model_name,
            app_name_ident=instance._meta.app_label,
            app_id_object=instance.id,
        )

# Динамически подписываем сигнал для каждой модели в TRACKED_MODELS
for model in TRACKED_MODELS:
    post_save.connect(create_notification, sender=model)

# Feedback(id, review_text, name, created_at, archived, is_approved, display_order)