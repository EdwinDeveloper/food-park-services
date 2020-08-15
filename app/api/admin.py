from django.contrib import admin

#Models
from .models import Owner , Pet , Service , Contract

# Register your models here.
admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Service)
admin.site.register(Contract)

