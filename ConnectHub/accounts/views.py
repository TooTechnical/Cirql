from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('profile')  # Redirect to a user profile or homepage
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# User Profile View
@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

