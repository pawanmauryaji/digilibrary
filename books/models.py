from django.db import models
from accounts.models import CustomUser


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta: 
        verbose_name = 'Category' 
        verbose_name_plural = 'Categories' 
    def __str__(self):
        return self.name
    

class DriveBooks(models.Model):
    LANGUAGE_CHOICES =[
        ('HINDI',"HINDI"),
        ('ENGLISH',"ENGLISH"),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    cover_image = models.ImageField(upload_to="books/cover_image/")
    drive_id = models.CharField(max_length=700)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    language = models.CharField(choices = LANGUAGE_CHOICES)
    total_pages = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'DriveBooks' 
        verbose_name_plural = 'Books' 
    
    def __str__(self):
        return f"{self.title}-{self.author}"
   



class Review(models.Model):
    RATING_CHOICES = [
    (1, "1 Star"),
    (2, "2 Star"),
    (3, "3 Star"),
    (4, "4 Star"),
    (5, "5 Star"),
    ]
    DriveBooks = models.ForeignKey(DriveBooks,on_delete=models.CASCADE)
    CustomUser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('DriveBooks','CustomUser')

    def __str__(self):
        return f"{self.rating} - { self.CustomUser }"

class Wishlist(models.Model):
    CustomUser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    DriveBooks = models.ForeignKey(DriveBooks,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('CustomUser','DriveBooks')

    def __str__(self):
        return f"{self.CustomUser}-{self.DriveBooks}"

