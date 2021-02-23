from uuid import uuid4

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

import datetime

# -----------------------------------------------------------------------------

# referral model
class Referral(models.Model):
    # referrer and referree as text field
    referrer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='referrer',
        null=True, blank=False,
        verbose_name=_("sent"),
        help_text=_("The user who referred a new user to Revibe.")
    )
    referree = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='referree',
        null=True, blank=False,
        verbose_name=_("referred"),
        help_text=_("the new user who was referred to Revibe.")
    )
    # field should accept either type of ip address
    ip_address = models.GenericIPAddressField(
        protocol='both',
        null=True, blank=True,
        help_text="IP address of new user."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.referrer} - {self.referree}"

    class Meta:
        verbose_name = "referral"
        verbose_name_plural = "referrals"