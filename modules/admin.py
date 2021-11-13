from django.contrib import admin

from modules.models import Contract, Event, Experts, Farmer, Investor, LocalGlobalMarket, New, Seminar, Service, Tips

# Register your models here.
# Sponsorships
admin.site.register(Farmer)
admin.site.register(Investor)
admin.site.register(Service)
admin.site.register(Contract)

# Collabration
admin.site.register(Seminar)
admin.site.register(Event)
admin.site.register(New)
admin.site.register(Tips)
admin.site.register(Experts)

# MarketPlace
admin.site.register(LocalGlobalMarket)