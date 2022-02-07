from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,UserProfileViewSet

router=routers.DefaultRouter()
router.register('',UserViewSet)
router.register('',UserProfileViewSet)
urlpatterns = [
    path('',include(router.urls))
]
