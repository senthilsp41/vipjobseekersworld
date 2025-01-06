from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your Username",
        'class': 'w-100 py-3 px-3 rounded'
    }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter your Password",
        'class': 'w-100 py-3 px-3 rounded'
    }))

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your Email",
        'class': 'w-100 py-3 px-3 rounded'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your Username",
        'class': 'w-100 py-3 px-3 rounded'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter your Password",
        'class': 'w-100 py-3 px-3 rounded'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm your Password",
        'class': 'w-100 py-3 px-3 rounded'
    }))
    profile_picture = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','profile_picture')
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        return email
class PasswordResetForm(forms.Form):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your new password'
        }),
        min_length=8,
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirm your new password'
        }),
        min_length=8,
    )

    # Validate the passwords match
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        new_password2 = cleaned_data.get('new_password2')

        if new_password and new_password2:
            if new_password != new_password2:
                raise forms.ValidationError("The two password fields must match.")
        return cleaned_data
    
    
class EmailForm(forms.Form):
    email = forms.EmailField(label="Enter your registered email")

# Form to collect OTP
class OTPForm(forms.Form):
    otp = forms.CharField(label="Enter the OTP", max_length=6)

# Form to collect new password
class NewPasswordForm(forms.Form):
    new_password = forms.CharField(label="Enter new password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm new password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


        
        

