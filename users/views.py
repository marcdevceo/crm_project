from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def login_user(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             # messages.success(request, "You Have Been Logged In!")
#             return redirect("home")
#         else:
#             messages.error(request, "There Was an Error Logging In, Please Try Again...")
#             return redirect("home")
#     else: 
#         return render(request, "home.html", {})


