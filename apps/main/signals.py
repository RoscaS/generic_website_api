from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

@receiver(post_save, sender=models.Message)
def send_message(instance, **kwargs):
    send_mail(
        subject=f"Nouveau message de {instance.name}",
        message=f"Message #{instance.pk} de {instance.email}\n"
                f"Le {instance.date.strftime('%d/%m/%y')} "
                f"à {instance.date.strftime('%H:%M')}\n"
                f"{instance.name} dit:\n\n"
                f"{instance.message}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_SEND_TO],
        fail_silently=False
    )
