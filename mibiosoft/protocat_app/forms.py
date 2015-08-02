from django import forms
from .models import Protocol, UserProfile, User
from django.core.exceptions import ValidationError
from django.utils import timezone

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        exclude = [None]
   
class ProtocolUploadForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = ['title', 'description', 'protocol_type', 'reagents', 'protocol']
        exclude = [None]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
