from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import auth, messages
from .models import Member
from .forms import SignUpForm

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = request.POST.get('password2')  

            if password == password2:
                if Member.objects.filter(email=email).exists():
                    messages.info(request, "Email has already been taken")
                    return redirect("register")

                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                
                user_login = auth.authenticate(username=email, password=password)
                if user_login:
                    auth.login(request, user_login)
                    return redirect('home')  
            else:
                messages.info(request, 'Passwords did not match')
        else:
            messages.error(request, 'Invalid form submission. Please correct the errors and try again.')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})




