from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

from users.models import Company

from .models import Service
from .forms import CreateNewService, RequestServiceForm

def home(request):
    # Get the most requested services
    most_requested = Service.objects.annotate(request_count=models.Count('requests')).order_by('-request_count')[:5]
    return render(request, 'main/home.html', {'most_requested': most_requested})


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    return render(request, 'services/create_service.html', {})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    return render(request, 'services/request_service.html', {})

# In services/views.py
@login_required
def create_service(request):
    if not request.user.is_company:
        messages.error(request, 'Only companies can create services.')
        return redirect('home')
    
    company = Company.objects.get(user=request.user)
    
    # Define choices based on company's field of work
    if company.field_of_work == 'All in One':
        choices = [
            ('Air Conditioner', 'Air Conditioner'),
            ('Carpentry', 'Carpentry'),
            ('Electricity', 'Electricity'),
            ('Gardening', 'Gardening'),
            ('Home Machines', 'Home Machines'),
            ('House Keeping', 'House Keeping'),
            ('Interior Design', 'Interior Design'),
            ('Locks', 'Locks'),
            ('Painting', 'Painting'),
            ('Plumbing', 'Plumbing'),
            ('Water Heaters', 'Water Heaters')
        ]
    else:
        choices = [(company.field_of_work, company.field_of_work)]
    
    if request.method == 'POST':
        form = CreateNewService(request.POST, choices=choices)
        if form.is_valid():
            # Create new service object
            service = Service(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                field=form.cleaned_data['field'],
                price_per_hour=form.cleaned_data['price_hour'],
                company=company
            )
            service.save()
            messages.success(request, 'Service created successfully!')
            return redirect('service_detail', service_id=service.id)
    else:
        form = CreateNewService(choices=choices)
    return render(request, 'services/create_service.html', {'form': form})