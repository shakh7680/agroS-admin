from django.urls import path
from . import views

urlpatterns = [
    # Sponsorships
    path('farmers', views.farmers, name='farmers'),
    path('investors', views.investors, name='investors'),
    path('farmer_services', views.farmer_services, name='farmer_services'),
    path('contracts', views.contracts, name='contracts')
]