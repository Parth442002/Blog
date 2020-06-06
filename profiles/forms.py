from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
    birthday=forms.DateField(help_text='Required. Format: YYYY-MM-DD',widget=forms.DateInput(attrs={'type':'date'}),input_formats='date')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta():
        model=Profile
        fields=('username','email','gender','birthday','aboutme','avatar','password')
        
