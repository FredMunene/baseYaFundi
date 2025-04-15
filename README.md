# BaseYaFundi

YaFundi is a service marketplace website designed to connect customers with companies offering various services. The platform supports two types of users: Companies and Customers.

## User Types

### Company
- Can create new services.
- Must provide the following information to register:
    - Email
    - Password
    - Password confirmation
    - Username
    - Field of work (e.g., Air Conditioner, Carpentry, Electricity, etc.)

### Customer
- Can request existing services.
- Must provide the following information to register:
    - Email
    - Password
    - Password confirmation
    - Username
    - Date of birth

## Registration and Login
- Both user types can register and login using their email and password.
- Each user must have a unique email and username.
- Users will be alerted if the email and/or username is already registered.

## User Profiles
- Each user has a profile page displaying their information (excluding the password).
- Customer profiles display all previously requested services.
- Company profiles display the services they provide.

## Services
- Companies can create services with the following attributes:
    - Name
    - Description
    - Field (must match the company's field of work, except for "All in One" companies)
    - Price per hour
    - Date created (automatically set)

## Service Categories
- The field of work for companies includes:
    - Air Conditioner
    - All in One
    - Carpentry
    - Electricity
    - Gardening
    - Home Machines
    - Housekeeping
    - Interior Design
    - Locks
    - Painting
    - Plumbing
    - Water Heaters

## Service Pages
- A page displaying the most requested services.
- A page showing all services in creation order (latest first).
- Category-specific pages displaying services available for each category.
- Individual service pages displaying detailed information and the providing company.

## Requesting Services
- Customers can request services by providing the address and service time needed.
- Requested services are added to the customer's list of previously requested services, showing:
    - Service name
    - Service field
    - Calculated service cost
    - Date requested
    - Providing company

## Navigation
- Users can navigate to company profiles from service pages to view all services offered by that company.

Enjoy using YaFundi to find and offer services efficiently!

## Technical Flow
```
manage.py >> netfix/settings.py >> netfix/urls.py >> root >> main/urls.py >> 
                                                  >> services >> services/url.py
                                                  >> users >> users/url.py
                                                




(Main)Base>Home>NavBar>Signup>> (users)>> Register (register.html)>> Customer
                                                                  >> Company:: CompanySignUp(view.py): register_company.html&CompnySignUpForm(form.py)
```


# Install virtualenv locally
```
pip install --user virtualenv
```
# Create a virtual environment
```
~/.local/bin/virtualenv venv
```
# Activate the virtual environment
```
source venv/bin/activate
```
# Install django
```
pip install django
```
# Apply migrations
```
python manage.py makemigrations app-name
python manage.py migrate
```

# Run the project
```
python manage.py runserver

```