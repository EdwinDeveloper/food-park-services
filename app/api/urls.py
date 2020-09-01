# DRF
from rest_framework import routers

from django.urls import path, include

from .views import OwnerViewSet, PetViewSet, ServiceViewSet, \
                   ContractViewSet, EstateViewSet, PropertyViewSet, \
                   LandLordViewSet, PayViewSet, ContractBuilderViewSet


router = routers.DefaultRouter()
router.register(r"owners", OwnerViewSet)
router.register(r"pets", PetViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"contracts", ContractViewSet)
router.register(r"estates", EstateViewSet)
router.register(r"properties", PropertyViewSet)
router.register(r"landlords", LandLordViewSet)
router.register(r"pays", PayViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/',
        include('rest_framework.urls', namespace="rest_framework")),
    path('new/', ContractBuilderViewSet.as_view(), name='')
]
