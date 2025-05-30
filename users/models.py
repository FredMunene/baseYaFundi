from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.CharField(max_length=100, unique=True)
# use models.EmailField instead of charField

class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # defines instances of user model as strings for debugging

    birth = models.DateField()  # mandatory birth date field
    def __str__(self):
        return self.user.username



class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    field_choices=(('Air Conditioner', 'Air Conditioner'),
                                                     ('All in One', 'All in One'),
                                                     ('Carpentry', 'Carpentry'),
                                                     ('Electricity','Electricity'),
                                                     ('Gardening', 'Gardening'),
                                                     ('Home Machines','Home Machines'),
                                                     ('House Keeping','House Keeping'),
                                                     ('Interior Design','Interior Design'),
                                                     ('Locks', 'Locks'),
                                                     ('Painting', 'Painting'),
                                                     ('Plumbing', 'Plumbing'),
                                                     ('Water Heaters', 'Water Heaters'))
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    field = models.CharField(max_length=70, choices=field_choices, blank=False, null=False)
    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username
