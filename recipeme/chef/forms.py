from django import forms

class UserSignupForm(forms.Form):
    username=forms.CharField(max_length=30)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    profile_picture=forms.URLField(max_length=100)
    password=forms.CharField(max_length=100)

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=100)