# DRF
from rest_framework import serializers
from datetime import datetime
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


class PropertySerializer(serializers.ModelSerializer):
    """Property model serializer"""
    class Meta:
        model = Property
        fields = "__all__"


class EstateSerializer(serializers.ModelSerializer):
    """Estate model serializer"""
    properties = PropertySerializer(many=True)
    class Meta:
        model = Estate
        fields = ("CODE", "ADDRESS", "PUBLIC_DEED", "properties")

    def create(self, validated_data):
        estate = Estate()
        estate.CODE = validated_data['CODE']
        estate.ADDRESS = validated_data['ADDRESS']
        estate.PUBLIC_DEED = validated_data['PUBLIC_DEED']
        estate.save()
        return estate


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

    def isofecha(self, tipo):
        if tipo == 'inicio':
            return datetime.now().replace(microsecond=0).isoformat()
        if tipo == 'final':
            return datetime.now().replace(microsecond=0).replace(year=datetime.now().year+1).isoformat()

    def create(self, validated_data):
        cn = Contract()
        pr = Property()
        pr.id = validated_data['DEPARTAMENTO']
        cn.NOMBRE_ARRENDADOR = validated_data['NOMBRE_ARRENDADOR']
        cn.NOMBRE_ARRENDATARIO = validated_data['NOMBRE_ARRENDATARIO']
        cn.SERVICIO_A_OFRECER = validated_data['SERVICIO_A_OFRECER']
        cn.FECHA_INICIO = ContractSerializer.isofecha(self, 'inicio')
        cn.FECHA_FINAL = ContractSerializer.isofecha(self, 'final')
        cn.PRECIO_INMUEBLE = validated_data['PRECIO_INMUEBLE']
        cn.PRECIO_DEPOSITO = validated_data['PRECIO_DEPOSITO']
        cn.MONTO_PENDIENTE = 0#validated_data['PRECIO_INMUEBLE'] + validated_data['PRECIO_DEPOSITO'] - validated_data['MONTO_ADELANTO']
        cn.PLAZO_GRACIA = validated_data['PLAZO_GRACIA']
        cn.PORCENTAJE_AUMENTO = validated_data['PORCENTAJE_AUMENTO']
        cn.DIRRECCION_ARRENDADOR = validated_data['DIRRECCION_ARRENDADOR']
        cn.DEPARTAMENTO = pr
        cn.save()
        return cn

