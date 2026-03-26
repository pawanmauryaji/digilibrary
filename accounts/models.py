from django.db import models



class CustomUser(models.Model):
    email = models.EmailField(primary_key=True)
    mobile = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="pictures/profile_pictures/",blank=True ,null=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'CustomUser' 
        verbose_name_plural = 'Users' 
    def __str__(self):
        return f"{self.email}"
    




