from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from services.models import Service
from django.db.models import Count

def home(request):
    # Most requested services
    most_requested = Service.objects.annotate(request_count=Count('requests')).order_by('-request_count')[:5]
    # Recently created services
    recent_services = Service.objects.all()[:5]
    
    return render(request, "main/home.html", {
        'most_requested': most_requested,
        'recent_services': recent_services,
    })


def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")
