from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserForm, LoginForm, EditProfileForm, ForgetPasswordForm,ChangePasswordForm
from .models import CustomUser
from books.models import Wishlist
from .utils import generate_otp, send_otp
from django.contrib import messages
import datetime
import json
import os
from django.conf import settings
import email


# Login Views
def login(request):

    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.objects.all().filter(email=email, password=password).first()  
            if user:
                request.session['email'] = email
                return redirect('profile')
            else:
                messages.error(request, "Invalid Email or Password")
                return redirect('login')
    else:
        form = LoginForm()           
    return render(request, 'accounts/login.html', {'form':form, 'error':error})

# Register Views
def register(request):

    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data["email"]
            otp = generate_otp()
            request.session["otp"] = otp
            request.session["register_data"] = request.POST.dict()
            request.session["otp_email"] = email
            request.session["purpose"] = "register"
            send_otp(email, otp)
            return redirect("verify_otp")
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})

# Verify OTP View
def verify_otp(request):
    
    purpose = request.session.get('purpose')
    otp = request.session.get('otp')
    otp_time = request.session.get('otp_time')

    if otp_time and (datetime.datetime.now().timestamp() - otp_time) > 300:
        messages.error(request, "OTP expired. Please resend.")
    email = request.session.get('otp_email')

    if request.method == "POST":
        user_otp = request.POST.get("otp")
        if user_otp == otp:
                

                if purpose == "forgot_password":
                    new_password = request.session.get('new_password')
                    user = CustomUser.objects.filter(email = email).first()
                    user.password = new_password
                    user.save()
                    messages.success(request, "Password Reset Successfully")
                    return redirect('login')
                    
                    
                
                if purpose == "register":
                    data = request.session.get("register_data")
                    form = CustomUserForm(data)
                    if form.is_valid():
                        password = form.cleaned_data.get('password') # user for somethig
                        form.save()
                        request.session.pop("otp", None)
                        request.session.pop("register_data", None)
                        messages.success(request, "Account created successfully. Please login.")
                        return redirect("login")
                    else:
                        messages.error(request,'Sorry You Filled Invalid Data in Form')
        else:   
            messages.error(request, "Invalid OTP. Please try again.")
    else:
        form = CustomUserForm()
    return render(request, "accounts/otp.html", {'email':email})

# Resend OTP View
def resend_otp(request):
    if not request.session.get('otp_email'):
        return redirect("register")
    
    otp = generate_otp()
    request.session["otp"] = otp
    send_otp(email, otp)
    return redirect("verify_otp")

# Forgot Password View
def forgot_password(request):
    if request.session.get('email'):
        return redirect('profile')
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            new_password = form.cleaned_data.get('password')

            user_exits = CustomUser.objects.filter(email=email).first()
            if user_exits:
                otp = generate_otp()
                send_otp(email,otp)
                request.session["otp"] = otp
                request.session["new_password"] = new_password
                request.session["otp_email"] = email
                request.session["purpose"] = "forgot_password"
                return redirect('verify_otp')
            else:
                messages.error(request,'Sorry User Not Registerd! ')
    else:
        form = ForgetPasswordForm()
    return render(request, 'accounts/forgot_password.html',{"form":form})

# Change Password View
def change_password(request):
    old_p = None
    email = request.session.get('email')
    if not email:
        return redirect('login')
    user = get_object_or_404(CustomUser,email=email)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_p = form.cleaned_data.get('old_password')
            new_p = form.cleaned_data.get('password')
        
        if user.password != old_p:
                form.add_error('old_password', "Your Old password is incorrect!")

        else:  
                user.password = new_p 
                user.save()
                return redirect('profile')
    else:
        form = ChangePasswordForm()
    
    return render(request, 'accounts/change_password.html',{'form':form})

# Profile View
def profile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    user = get_object_or_404(CustomUser, email=email)
    wishlist = Wishlist.objects.filter(CustomUser=user)
    return render(request, 'accounts/profile.html', {'user': user,'wishlist':wishlist})
    
# Edit Profile View
def edit_profile(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    user = get_object_or_404(CustomUser, email=email)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form, 'user': user})

# Logout View
def logout(request):
    request.session.flush()    
    return redirect('home')



