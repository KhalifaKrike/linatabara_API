from django.contrib import admin
from .models import Donor, Daiira, Wilaya,BloodType
# Register your models here.
admin.site.register(Wilaya)
admin.site.register(Daiira)
admin.site.register(BloodType)
admin.site.register(Donor)


