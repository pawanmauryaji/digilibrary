from django.shortcuts import render,redirect
from books.models import DriveBooks
from .forms import ContactFrom

# Home Page View
def index(request):
    allbooks = DriveBooks.objects.all()
    request.session.get('email')
    return render(request,'core/index.html',{"allbooks":allbooks})

# About Page View
def about(request):
    return render(request,'core/about.html')

# Contact Page View
def contact(request):

    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')     
    else:
        form = ContactFrom()
    return render(request,'core/contact.html',{'form':form})

# Social Page View
def social(request):
    return render(request,'core/social.html')






