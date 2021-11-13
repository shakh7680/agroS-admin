from django.shortcuts import render
from django.core.paginator import Paginator
from modules.models import Contract, DeliveryOfGoods, Event, Experts, Farmer, Fertilizer, Investor, LocalGlobalMarket, MachineOwners, Machines, Seminar,Service, New, Tips

# Create your views here.
# Sponsorships
def farmers(request):
    farmers = Farmer.objects.all()
    context = {
        'farmers': farmers
    }
    return render(request, 'sponsorship/farmers.html', context)

def investors(request):
    investors = Investor.objects.all()
    context = {
        'investors': investors
    }
    return render(request, 'sponsorship/investors.html', context)
    
def farmer_services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'sponsorship/farmer_services.html', context)

def contracts(request):
    contracts = Contract.objects.all()
    context = {
        'contracts': contracts
    }
    return render(request, 'sponsorship/contracts.html', context)

# Collabrations
def seminars(request):
    seminars = Seminar.objects.all()
    context = {
        'seminars': seminars
    }
    return render(request, 'collabration/online_seminars.html', context)

def events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'collabration/offline_events.html', context)

def news(request):
    news = New.objects.all()
    context = {
        'news': news
    }
    return render(request, 'collabration/news.html', context)

def tips(request):
    tips = Tips.objects.all()
    context = {
        'tips': tips
    }
    return render(request, 'collabration/tips.html', context)

def experts(request):
    experts = Experts.objects.all()
    context = {
        'experts': experts
    }
    return render(request, 'collabration/experts.html', context)

# Marketplace
def local_market(request):
    local_markets = LocalGlobalMarket.objects.filter(local_global = False)
    paginator = Paginator(local_markets,4)
    page = request.GET.get('page')
    local_markets = paginator.get_page(page)
    context = {
        'local_markets': local_markets
    }
    return render(request, 'market/local_market.html', context)

def global_market(request):
    global_markets = LocalGlobalMarket.objects.filter(local_global = True)
    context = {
        'global_markets': global_markets
    }
    return render(request, 'market/global_market.html', context)

def fertilizer(request):
    fertilizers = Fertilizer.objects.all()
    context = {
        'fertilizers': fertilizers
    }
    return render(request, 'market/fertilizers/all_types.html', context)

def delivery(request):
    deliveries = DeliveryOfGoods.objects.all()
    context = {
        'deliveries' : deliveries
    }
    return render(request, 'market/logistics.html', context)

# Machine Renting
def machine_owners(request):
    owners = MachineOwners.objects.all()
    context = {
        'owners' : owners
    }
    return render(request, 'machine_renting/machine_owners.html', context)

def renting_machines(request):
    rented_machines = Machines.objects.all()
    context = {
        'rented_machines' : rented_machines
    }
    return render(request, 'machine_renting/renting_machines.html', context)

def available_machines(request):
    available_machines = Machines.objects.all()
    context = {
        'available_machines' : available_machines
    }
    return render(request, 'machine_renting/available_machines.html', context)

# Info about farmer
def farmer(request,id):
    farmer_info = Farmer.objects.get(id=id)
    context = {
        'farmer_info' : farmer_info
    }
    return render(request, 'sponsorship/farmer_info.html', context)
