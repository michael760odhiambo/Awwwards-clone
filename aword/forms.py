from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['username', 'post_date', 'pic']
        widgets = {
            'technologies':forms.CheckboxSelectMultiple(),
            'categories':forms.CheckboxSelectMultiple(),
            'countries':forms.CheckboxSelectMultiple(),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )        