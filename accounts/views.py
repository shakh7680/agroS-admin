from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
# 
def home(request):
    return render(request, 'home.html')


# Registration
def register(request):
    if request.method == 'POST':
        #Get from values
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        #Check if passwords are similar
        if password == password2:
            #Username is checked
            if User.objects.filter(email=email).exists():
                messages.error(request, "That email is already taken!")
                return redirect('register')
            else:
                #Looks OK                
                user= User.objects.create_user( password=password, email=email)
                user.save()
                redirect('login')  
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# Login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are logged in!')
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request,'Invalid ceradentials!')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def admin_dashboard(request): 
    return render(request, 'accounts/admin/admin_dashboard.html')

def dashboard(request): 
    return render(request, 'accounts/dashboard.html')

# Logout
def logout(request):
    auth.logout(request)
    return redirect('home')