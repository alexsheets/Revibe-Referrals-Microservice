from django.db.models import Q
from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes


from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenMatchesOASRequirements 

from django.utils.http import is_safe_url
from django.shortcuts import redirect
from django.contrib import auth

from referrals.exceptions import *
from referrals.responses import *
from .models import Referral
from .serializer import ReferralSerializer

#---------------------------------------------------------------------------


class ReferralViewSet(viewsets.ModelViewSet):
    serializer_class = ReferralSerializer
    permission_classes = [
        TokenMatchesOASRequirements,
    ]
    
    required_alternate_scopes = {
        "GET": [["ADMIN"], ["read", "write"]],
        "POST": [["ADMIN"], ["read", "write"]],
    }

    def get_queryset(self):
        user = self.request.user
        return Referral.objects.filter(Q(referrer=user) | Q(referree=user))

    def update(self, request, pk=None, *args, **kwargs):
        raise exceptions.MethodNotAllowed("Referrals cannot be edited.")
    def destroy(self, request, pk=None, *args, **kwargs):
        raise exceptions.MethodNotAllowed("Referrals cannot be deleted.")

