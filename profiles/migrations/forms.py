from django import forms
from .models import Profile

class RegistrationForm(forms.ModelForm):
    birthday=forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta():
        model=Profile
        fields=('username','email','gender','birthday','aboutme','avatar','password')

