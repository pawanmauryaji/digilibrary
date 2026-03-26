from django.urls import path
from . import views

urlpatterns = [
    path('all-books/',views.allbooks, name="allbooks"),
    path('detail-book/<int:book_id>/',views.detail_book, name="detail_book"),
    path('read-book/<int:book_id>/',views.read_book, name="read_book"),
    path('download/',views.download, name="download"),
    path('toggle_wishlist/<int:book_id>/', views.toggle_wishlist, name="toggle_wishlist"),

]
