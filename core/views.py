#from django.shortcuts import render
#from django.http import HttpResponse
from .models import Student 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required # Protects pages
from .forms import RegisterForm # Import the form we just made
from django.shortcuts import render, redirect # Import the model

# View for the Home Page
'''def home(request):
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
    return render(request, 'contact.html')'''


def home(request):
    # Fetch ALL students from the database
    all_students = Student.objects.all()
    # Send the data to the template inside a 'context' dictionary
    return render(request, 'home.html', {'students': all_students})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Saves the user to DB
            login(request, user) # Auto-login after registration
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# 2. LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the user object from the form
            user = form.get_user()
            login(request, user) # Starts the session
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. LOGOUT VIEW
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

# 4. DASHBOARD (Protected Page)
@login_required(login_url='login') # Redirects to login if not signed in
def dashboard(request):
    return render(request, 'dashboard.html')