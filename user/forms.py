from django import forms
from django.contrib.auth.models import User

from general.utility.enums import GenderEnum, WorkingModelEnum
from user.models import CareerProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=75, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label="Email")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}), label="İsim")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}), label="Soyisim")
    gender = forms.ChoiceField(choices=GenderEnum.choices(), required=True, label="Cinsiyet")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'gender']

    def save(self, commit=True, *args, **kwargs):
        gender = self.cleaned_data.pop('gender', None)
        self.cleaned_data.pop('profile_status', None)
        user = super(UserForm, self).save(*args, **kwargs)
        user.profile.gender = gender
        user.profile.save()
        return user


class CareerProfileForm(forms.ModelForm):
    job = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aranan Pozisyon'}), label="Pozisyon")

    class Meta:
        model = CareerProfile
        fields = ['cv', 'job', 'working_model', 'location']
