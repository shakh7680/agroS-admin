from django.contrib import admin

from modules.models import Contract, Farmer, Investor, Service

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Investor)
admin.site.register(Service)
admin.site.register(Contract)