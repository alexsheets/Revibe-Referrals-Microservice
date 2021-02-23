from django.urls import reverse
from ReferralService.models import Referral
from django.test import TestCase
from django.contrib.auth.models import User

#-------------------------------------------------------------------------------

class ReferralTestCase(TestCase):
    def setUp(self):
        self.application = 'referrals'
        # user = User.objects.create()
    
    # def test_create_referral(self):
    #     """
    #     Ensures creation of a referral is possible.
    #     """
    #     data = {
    #         "user_id": user.id 
    #     }
    #     referral = Referral.objects.create(
    #         referrer=referrer,
    #         referree=user
    #     )

    def test_view_referrals(self):
        url = reverse('referrals-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)