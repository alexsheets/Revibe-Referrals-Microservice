from django.core.validators import ip_address_validators
from django.core.exceptions import ValidationError

from .utils.params import get_url_param
from .models import Referral

# -----------------------------------------------------------------------------

def attach_referral(referrer, referree, **validated_data):
    # create check to see if new user has already been referred
    # num = Referral.objects.filter(referree=referree).count()
    # if num > 0:
    #     raise Exception("User has already been referred to our services.")

    # check that user has registered within allowed time
    
    # create referral object
    referral = Referral.objects.create(
        referrer=referrer,
        referree=referree,
        **validated_data
    )
    # return the referral object
    return referral

def get_referral(referree, referrer):
    kwargs = {
        "referree": referree
    }
    if referrer:
        kwargs['referrer'] = referrer
    
    try:
        referral = Referral.objects.get(**kwargs)
    except Exception:
        return None
    
    return referral