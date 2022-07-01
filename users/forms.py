from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProfilePicture
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class':'form-control', 'id':'input-file'}),
        }