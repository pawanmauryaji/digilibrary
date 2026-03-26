from django.contrib import admin

from .models import Publisher,Author,Category,DriveBooks,Review,Wishlist

# class PulisherAdmin(admin.AdminModel):
#     list_display = ('name', 'address', ) 
#     search_fields = ('name', 'address')           
admin.site.register(Publisher)



admin.site.register(Author)
admin.site.register(Category)
admin.site.register(DriveBooks)
admin.site.register(Review)
admin.site.register(Wishlist)
