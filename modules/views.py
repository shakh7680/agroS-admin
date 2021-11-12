from django.shortcuts import render

from modules.models import Contract, Farmer, Investor,Service

# Create your views here.
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
    