# DRF
from rest_framework import serializers

# Models

from .models import Owner, Pet, Service, \
                    Contract, Estate, Property, LandLord, Pay


class OwnerSerializer(serializers.ModelSerializer):
    """Owner model serializer"""
    class Meta:
        model = Owner
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
    """Pet model serializer"""
    class Meta:
        model = Pet
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    """Service model serializer"""
    class Meta:
        model = Service
        fields = "__all__"


class EstateSerializer(serializers.ModelSerializer):
    """Estate model serializer"""
    class Meta:
        model = Estate
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    """Property model serializer"""
    class Meta:
        model = Property
        fields = "__all__"


class LandLordSerializer(serializers.ModelSerializer):
    """LandLord model serializer"""
    class Meta:
        model = LandLord
        fields = "__all__"


class PaySerializer(serializers.ModelSerializer):
    """Pay Serializers"""
    class Meta:
        model = Pay
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    """Contract model serializer"""
    class Meta:
        model = Contract
        fields = "__all__"
