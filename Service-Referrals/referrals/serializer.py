from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Referral
from .referral import attach_referral

#------------------------------------------------------------------------------

class ReferralSerializer(serializers.ModelSerializer):
    referree = serializers.CharField(source='referree.username', read_only=True)
    referrer = serializers.CharField(source='referrer.username')
    ip_address = serializers.CharField(source='referree_ip_address', required=False)

    class Meta:
        model = Referral
        fields = [
            'id',
            'referrer',
            'referree',
            'ip_address'
        ]
        read_only_fields = [
            'id',
        ]

        def create(self, validated_data, *args, **kwargs):
            user = None
            request = self.context.get('request', None)
            if request and hasattr(request, 'user'):
                user = request.user
            else:
                # serializer validation error
                raise Exception("Could not identify the user in request.")

            referrer_username = validated_data.pop('referrer')['username']
            referrer = get_object_or_404(get_user_model(), username=referrer_username)

            # create instance
            instance = attach_referral(referrer=referrer, referree=user, **validated_data)

            return instance
        
        def update(self, instance, validated_data, *args, **kwargs):
            # serviceunavailableerror
            raise Exception("Cannot edit referrals")
