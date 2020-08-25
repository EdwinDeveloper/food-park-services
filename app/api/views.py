# DRF
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import OwnerSerializer, PetSerializer, ServiceSerializer, \
                         ContractSerializer, EstateSerializer, \
                         PropertySerializer, \
                         LandLordSerializer, PaySerializer
from .models import Owner, Pet, Service, Contract, Estate, \
                    Property, LandLord, Pay


# Create your views here.
class OwnerViewSet(viewsets.ModelViewSet):
    """Owner view set"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Owner.objects.all().order_by("first_name")
    serializer_class = OwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    """Pet view set"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all().order_by("name")
    serializer_class = PetSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """Service view set"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all().order_by("date")
    serializer_class = ServiceSerializer


class ContractViewSet(viewsets.ModelViewSet):
    """Contract view set"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Contract.objects.all().order_by("NOMBRE_ARRENDATARIO")
    serializer_class = ContractSerializer


class EstateViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Estate.objects.all().order_by("CODE")
    serializer_class = EstateSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all().order_by("CODE")
    serializer_class = PropertySerializer


class LandLordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = LandLord.objects.all().order_by("NAME_LANDLORD")
    serializer_class = LandLordSerializer


class PayViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Pay.objects.all().order_by("FECHA")
    serializer_class = PaySerializer
