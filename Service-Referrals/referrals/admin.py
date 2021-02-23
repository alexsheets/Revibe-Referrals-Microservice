from django.contrib import admin
from .models import *


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    pass
