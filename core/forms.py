from django import forms
from .models import Contact


class ContactFrom(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder':'Your Name',
            }),
            'email':forms.TextInput(attrs={
                'class':'w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder':'Your Email',

            }),
            'message':forms.Textarea(attrs={
            'class':'w-full p-3 rounded-2xl h-[120px] md:h-[150px] bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none',
            'placeholder':'Your Message',
            }),
        }
