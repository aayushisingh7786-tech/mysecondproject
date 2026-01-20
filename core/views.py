from django.shortcuts import render
from django.http import HttpResponse
from .models import Student # Import the model

# View for the Home Page
def home(request):
    """
    Renders the 'home.html' template for the home page.
    """
    # Assuming 'home.html' is in the templates directory of an app
    return render(request, 'home.html')

# View for the About Page
def about(request):
    """
    Renders the 'about.html' template for the about page.
    """
    # Assuming 'about.html' is in the templates directory of an app
    return render(request, 'about.html')

# View for the Contact Page
def contact(request):
    """
    Renders the 'contact.html' template for the contact page.
    """
    # Assuming 'contact.html' is in the templates directory of an app
    return render(request, 'contact.html')


def home(request):
    # Fetch ALL students from the database
    all_students = Student.objects.all()
    # Send the data to the template inside a 'context' dictionary
    return render(request, 'home.html', {'students': all_students})
