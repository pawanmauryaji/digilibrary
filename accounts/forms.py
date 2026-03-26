from django import forms
from .models import CustomUser


# Register Form
class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Enter Password",
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Confirm Password",
        })
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile', 'password']
        widgets = {
            'first_name':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter First Name", }),

            'last_name':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter Last Name", }),
        
            'email':forms.EmailInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                 "placeholder":"Enter Your Email", }),
        
            'mobile':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                 "placeholder":"Enter Mobile No.", }),
    
            }
        error_messages = {
            'email': {
                'unique': "User Already Registerd ! ",
            }
        }
    
    def clean(self):
        cleaned_data = super().clean()
        
        # First Name 
        first_name = cleaned_data.get('first_name')
        if first_name:
            if not first_name.isalpha(): 
                self.add_error("first_name", "Please Enter a Valid Name!")
            else:
                cleaned_data['first_name'] = first_name.lower()
        
        # Last Name 
        last_name = cleaned_data.get('last_name')
        if last_name: 
            if not last_name.isalpha(): 
                self.add_error("last_name", "Please Enter a Valid Name!")
            else:
                cleaned_data['last_name'] = last_name.lower()

        # Email
        email = cleaned_data.get('email')
        if email:
            cleaned_data['email'] = email.lower()

        # Mobile
        mobile = cleaned_data.get('mobile')
        if mobile: 
            if not mobile.isdigit():
                self.add_error("mobile", 'Please Enter a valid Mobile Number!')
            elif len(mobile) != 10: 
                self.add_error("mobile", "Mobile number must be 10 digits!")

        # Password 
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password:
            if len(password) <8:
                self.add_error('password',"password must be 8 digits! ")
            elif password.isdigit():
                self.add_error('password','Password must contain both letters and numbers.')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data


# Login Form
class LoginForm(forms.Form):
            
            email = forms.EmailField(widget=forms.EmailInput(attrs={
                  "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter Your Email",
            }))

            password = forms.CharField(widget=forms.PasswordInput(attrs={
                  "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter Your Password",
            
            }))


# Edit Profile Form 
class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
           
        }),
         required=False,
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile','profile_pic']
        widgets = {
            'first_name':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter First Name", }),

            'last_name':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                "placeholder":"Enter Last Name", }),
        
            'email':forms.EmailInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                 "placeholder":"Enter Your Email",
                  'readonly':'readonly', }),
        
            'mobile':forms.TextInput(attrs={
                "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
                 "placeholder":"Enter Mobile No.", }),
               
        }

    def clean(self):
        cleaned_data = super().clean()
        
        # First Name 
        first_name = cleaned_data.get('first_name')
        if first_name:
            if not first_name.isalpha(): 
                self.add_error("first_name", "Please Enter a Valid Name!")
            else:
                cleaned_data['first_name'] = first_name.lower()
        
        # Last Name 
        last_name = cleaned_data.get('last_name')
        if last_name: 
            if not last_name.isalpha(): 
                self.add_error("last_name", "Please Enter a Valid Name!")
            else:
                cleaned_data['last_name'] = last_name.lower()

        # Mobile
        mobile = cleaned_data.get('mobile')
        if mobile: 
            if not mobile.isdigit():
                self.add_error("mobile", 'Please Enter a valid Mobile Number!')
            elif len(mobile) != 10: 
                self.add_error("mobile", "Mobile number must be 10 digits!")

        return cleaned_data
    

# ForgetPassword Form
class ForgetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Enter new Password",
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Confirm  Password",
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
             "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Enter Your Registerd Email",

        })
    )

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password:
            if len(password) < 8:
                self.add_error('password', 'Passowrd must be contain 8 digits')
            elif password.isdigit():
                self.add_error('password','Password must contain both letters and numbers.')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

# Change Password Form
class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Enter Your Old Password",
            
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Enter Your New Password",
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"w-full p-3 rounded-2xl bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400 transition",
            "placeholder":"Confirm Your Password",
        })
    )
    class Meta:
        model = CustomUser
        fields = ['password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password:
            if len(password) < 8:
                self.add_error('password', "Password Must be contain 8 digits! ")
            elif password.isdigit():
                self.add_error('password','Password must contain both letters and numbers.')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")