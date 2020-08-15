from django.db import models


# Create your models here.
class Owner(models.Model):
    """Owner model"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    """Pet Model"""
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight = models.FloatField()
    size = models.FloatField()
    photo = models.URLField()

    # Relations
    owner = models.ForeignKey(Owner,
                              related_name="pets", on_delete=models.CASCADE)

    def __str__(self):
        """Return pet name"""
        return self.name


class Service(models.Model):
    """Service model"""
    type = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # Relations
    pet = models.ForeignKey(Pet,
                            related_name="services", on_delete=models.CASCADE)

    def __str__(self):
        """Return Pet Name and Type Service"""
        return f"Pet : {self.pet} servicio : {self.type}"


class Estate(models.Model):
    """Estate model"""
    CODE = models.CharField(max_length=100)
    ADDRESS = models.CharField(max_length=500)
    PUBLIC_DEED = models.CharField(max_length=200)

    def __str__(self):
        """Return Public deed"""
        return self.CODE


class Property(models.Model):
    """Property model"""
    CODE = models.CharField(max_length=10)
    DESCRIPTION = models.CharField(max_length=500)
    PRICE = models.FloatField()
    DEPOSIT = models.FloatField()
    PERCENT_INCREASE = models.FloatField()
    type = models.CharField(max_length=50)

    # Relations
    estate = models.ForeignKey(Estate,
                               related_name="properties",
                               on_delete=models.CASCADE)

    def __str__(self):
        """Return Property code"""
        return self.CODE

    def __PRICE__(self):
        """Return PRICE"""
        return self.PRICE


class Pay(models.Model):
    """Pay model"""
    FECHA = models.DateTimeField(auto_now_add=True)
    MONTO = models.FloatField()
    RESTANTE = models.FloatField(null=True, blank=True, default=None)
    FECHA_LIMITE = models.DateTimeField()

    # Relations
    property = models.ForeignKey(Property,
                                 related_name="pays",
                                 blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        """Return pago"""
        return self.FECHA


class LandLord(models.Model):
    NAME_LANDLORD = models.CharField(max_length=200)
    ADDRESS = models.CharField(max_length=500)
    CURP = models.CharField(max_length=18)

    def __str__(self):
        """Return LandLord Name"""
        return f"LandLord name : {self.NAME_LANDLORD}"


class Contract(models.Model):
    """Contract model"""
    NOMBRE_ARRENDADOR = models.CharField(max_length=255)
    NOMBRE_ARRENDATARIO = models.CharField(max_length=255)

    NUMERO_ESCRITURA = ""
    TIPO_INMUEBLE = ""
    DIRECCION_INMUEBLE = ""

    SERVICIO_A_OFRECER = models.CharField(max_length=255)

    FECHA_INICIO = ""
    FECHA_FINAL = ""

    # PRECIO_INMUEBLE = models.CharField(max_length=5)
    DEPARTAMENTO = models.ForeignKey(Property,
                                     related_name="contracts",
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE)
    PRECIO_DEPOSITO = models.CharField(max_length=5)
    PLAZO_GRACIA = models.CharField(max_length=1)
    PORCENTAJE_AUMENTO = models.CharField(max_length=3)
    DIRRECCION_ARRENDADOR = models.CharField(max_length=500)

    # buildContract()

    def __str__(self):
        """Return Arrendatario nombre"""
        return f"Contrato a nombre de : {self.NOMBRE_ARRENDATARIO}"
