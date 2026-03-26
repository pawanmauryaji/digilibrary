from django.shortcuts import render,redirect,get_object_or_404
from .models import DriveBooks,Wishlist,Review
from accounts.models import CustomUser
from .forms import SerachBooksForm,ReviewForm
from django.db.models import Q,Avg
from django.contrib import messages




def allbooks(request):
    email = request.session.get('email')
    modal = False
    allbooks = DriveBooks.objects.all()
    books = DriveBooks.objects.all()
    if request.method == "POST":
        modal_value = request.POST.get('modal')
        if modal_value == "open":
            modal =True

    form = SerachBooksForm(request.GET or None )
    if form.is_valid():
        query = form.cleaned_data.get('query','')
        if query:
            books = books.filter(
                Q(title__icontains = query) |
                Q(author__name__icontains = query) |
                Q(category__name__icontains = query)
            )
    context = {"allbooks":allbooks,'modal':modal,'form':form,'books':books}
    return render(request,'books/allbooks.html',context)


def detail_book(request, book_id ):
    email = request.session.get('email')
    if not email:
        return redirect('allbooks')
    book = get_object_or_404(DriveBooks, id = book_id)

    user = CustomUser.objects.filter(email=email).first()
    wishlist_queryset = Wishlist.objects.filter(CustomUser=user)
    wishlist_books = [w.DriveBooks for w in wishlist_queryset]

    user_review = None
    all_reviews = Review.objects.filter(DriveBooks_id=book_id)

    avg_result = all_reviews.aggregate(Avg('rating'))
    average_rating = avg_result['rating__avg']

    if email:
        user_review = all_reviews.filter(CustomUser=user).first()
        other_reviews = all_reviews.exclude(CustomUser=user)

    if request.method == 'POST':
      form = ReviewForm(request.POST, instance=user_review) 
    
      if form.is_valid():
        review = form.save(commit=False)
        review.DriveBooks = book
        review.CustomUser = user
        review.save()
        
       
        if user_review:
            messages.success(request, 'Review updated successfully!')
        else:
            messages.success(request, 'Review submitted successfully!')
            
        return redirect('detail_book', book_id=book.id)
    else:
    
       form = ReviewForm(instance=user_review)

    context ={'book':book,'form':form,'wishlist_books':wishlist_books,'user_review':user_review,'other_reviews':other_reviews,'average_rating':average_rating}
    return render(request,'books/detail_book.html',context)


def toggle_wishlist(request, book_id):
    user_email = request.session.get('email')
    if not user_email: 
        return redirect('login')
     
    if request.method == 'POST':
        book = get_object_or_404(DriveBooks, id=book_id)
        user = get_object_or_404(CustomUser, email=user_email)
        wishlist_item = Wishlist.objects.filter(CustomUser=user, DriveBooks=book)
        if wishlist_item.exists():
            wishlist_item.delete() 
        else:
            Wishlist.objects.create(CustomUser=user, DriveBooks=book)    
    return redirect('detail_book', book_id=book_id)


def download(request):
    if not request.session.get('email'):
        return redirect('home')
    return render(request,'books/download.html')


import base64

def read_book(request, book_id):
    email = request.session.get('email')
    if not email:
        return redirect('allbooks')
    
   
    book = get_object_or_404(DriveBooks,id=book_id)
    Drive_id = book.drive_id

    raw_url = f"https://drive.google.com/file/d/{Drive_id}/preview"

    # Python mein string ko pehle .encode() karna padta hai
    url_bytes = raw_url.encode("ascii")
    base64_bytes = base64.b64encode(url_bytes)
    url_final = base64_bytes.decode("ascii")

    context = {'url': url_final,'book':book}
    return render(request, 'books/read_drive_book.html', context)