from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.conf import settings

from .views import ReferralViewSet

#-------------------------------------------------------------------------------

router = routers.DefaultRouter()
router.register('', ReferralViewSet, basename="referrals")

urls = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

base_path = settings.APPLICATION_NAME.lower().replace('_', '-')
urlpatterns = [
    path(f"api/{base_path}/", include(urls)),
]