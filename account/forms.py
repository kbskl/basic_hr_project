from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

from general.utility.enums import GenderEnum, ProfileStatusEnum


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=75,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid email and password has been entered.')


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=75,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Tekrar Parola'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}))
    gender = forms.ChoiceField(choices=GenderEnum.choices(), required=True, label="Cinsiyet")
    profile_status = forms.ChoiceField(choices=ProfileStatusEnum.choices(), required=True, label="Profil")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "gender", "profile_status"]

    def save(self, commit=True, *args, **kwargs):
        gender = self.cleaned_data.pop('gender', None)
        profile_status = self.cleaned_data.pop('profile_status', None)
        user = super(RegisterForm, self).save(*args, **kwargs)
        user.profile.gender = gender
        user.profile.profile_status = profile_status
        user.profile.save()
        return user


class UserPasswordChangeForm(PasswordChangeForm):
    user = None
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Eski Parola'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Parola'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Tekrar Yeni Parola'}))

    def save(self, commit=True):
        data = super(UserPasswordChangeForm, self).save(commit=False)
        data.email = data.username
        data.save()
        return data


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Parola'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Tekrar Yeni Parola'}))
