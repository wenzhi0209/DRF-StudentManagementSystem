from django.urls import path,include
from rest_framework import routers
from .views import WaitlistEntryViewSet

router=routers.DefaultRouter()
router.register('',WaitlistEntryViewSet)

urlpatterns = [
    path('',include(router.urls))
]