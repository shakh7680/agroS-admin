from django.urls import path
from . import views

urlpatterns = [
    # Sponsorships
    path('farmers', views.farmers, name='farmers'),
    path('investors', views.investors, name='investors'),
    path('farmer_services', views.farmer_services, name='farmer_services'),
    path('contracts', views.contracts, name='contracts'),

    # Collaboration
    path('experts', views.experts, name='experts'),
    path('tips', views.tips, name='tips'),
    path('news', views.news, name='news'),
    path('events', views.events, name='events'),
    path('seminars', views.seminars, name='seminars'),

    # Marketplace
    path('local_market', views.local_market, name='local_market'),
    path('global_market', views.global_market, name='global_market'),
    path('fertilizer', views.fertilizer, name='fertilizer'),
    path('delivery', views.delivery, name='delivery'),

    # Machine Renting
    path('machine_owners', views.machine_owners, name='machine_owners'),
    path('renting_machines', views.renting_machines, name='renting_machines'),
    path('available_machines', views.available_machines, name='available_machines'),
    
    # Info about farmer
    path('farmer/<int:id>', views.farmer, name='farmer')
]