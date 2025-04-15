from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseServerError

from users.models import User, Company
from services.models import Service


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request, name=None):
    """
    Display customer profile based on URL pattern /customer/<slug:name>
    Example: /customer/fred-6368
    """

    try:
        # Get the customer directly from the User model
        user = get_object_or_404(User, username=name, is_customer=True)

        context = {
            'customer': user,
            'user': user,
        }
        
        return render(request, 'users/profile.html',context )
    
    except Exception as e:
        # Log the error for debugging
        print(f"Error in customer_profile: {str(e)}")
        return HttpResponseServerError("An error occurred while retrieving the customer profile")


def company_profile(request, name):
    # fetches the company user and all of the services available by it
    user = User.objects.get(username=name)
    services = Service.objects.filter(
        company=Company.objects.get(user=user)).order_by("-date")

    return render(request, 'users/profile.html', {'user': user, 'services': services})
