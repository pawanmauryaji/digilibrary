from django import forms
from .models import Review

# Search Books Form
class SerachBooksForm(forms.Form):
    query =forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            "class":"p-3 text-sm md:text-xl border-2 border-transparent rounded-l-xl w-full h-[50px] md:w-2xl focus:outline-0 text-white",
            "placeholder": "Seacrh Books by title, author or category....."
        })
        )




# Review Form
class ReviewForm(forms.ModelForm):

    
    class Meta:
        model=Review
        fields =['rating','comment']
        
      
        RATING_CHOICES=[
        (1,"1 star"),
        (2,"2 star"),
        (3,"3 star"),
        (4,"4 star"),
        (5,"5 star")
    ]
        widgets ={
            'rating':forms.Select(choices=RATING_CHOICES,attrs={
                'class':'p-3 text-sm md:text-xl border-2 border-transparent rounded-l-xl w-full h-[50px] md:w-2xl focus:outline-0 text-black'

            }),

            'comment':forms.TextInput(attrs={
                'class':'p-3 text-sm md:text-xl border-2 border-transparent rounded-l-xl w-full h-[50px] md:w-2xl focus:outline-0 text-white',
                'placeholder':'Write a Review'
            })
        }



