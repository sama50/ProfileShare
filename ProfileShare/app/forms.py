from django import forms
from app.models import Details ,LinkData , ProjectDetails , Achivement
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'email', 'password1', 'password2']
  labels = {'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))


class uploadimg(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'Education', 'email', 'image']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'Education':forms.Select(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})} 

class AddLink(forms.ModelForm):
    class Meta:
        model = LinkData
        fields = ['nameLink','link']
        widgets = { 'nameLink':forms.TextInput(attrs={'class':'form-control'}),'link':forms.TextInput(attrs={'class':'form-control'}) }


class AddProjectDetails(forms.ModelForm):
    class Meta:
        model = ProjectDetails
        fields = ['projectname','githublink','image1','image2','desc']
        widgets = { 'projectname':forms.TextInput(attrs={'class':'form-control'}),'githublink':forms.URLInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}

class AddAchivement(forms.ModelForm):
    class Meta:
        model = Achivement
        fields = ['nameofachivement']
        widgets = {'nameofachivement':forms.Textarea(attrs={'class':'form-control'})}