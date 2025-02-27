from django.db.models.signals import post_save
from main_app.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.urls import reverse


@receiver(post_save, sender=User)
def user_update(sender, instance, *args, **kwargs):
    if not instance.is_verified:
        send_mail(
            'Verify your account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
            'admin@localhost.ru',
            [instance.email],
            fail_silently=False,
        )