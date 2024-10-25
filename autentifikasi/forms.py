from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    budget = forms.IntegerField(required=False, label="Budget")
    profile_image = forms.URLField(required=False, label="Profile Image URL")  # Menggunakan URLField

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role', 'budget', 'profile_image']

class EditProfileForm(forms.ModelForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    budget = forms.IntegerField(required=False, label="Budget")
    profile_image = forms.URLField(required=False, label="Profile Image URL")  # Ganti menjadi URLField

    class Meta:
        model = User
        fields = ['username', 'budget', 'profile_image']

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if profile:
            self.fields['role'].initial = profile.role
            self.fields['budget'].initial = profile.budget
            self.fields['profile_image'].initial = profile.profile_image  # Isi dengan URL gambar yang ada
