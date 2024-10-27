from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    budget = forms.IntegerField(required=False, label="Budget")
    profile_image = forms.URLField(required=False, label="Profile Image URL")

    class Meta:
        model = User
        # Password1 dan password2 sudah ada dari UserCreationForm
        # Role tidak perlu di fields karena sudah didefinisikan sebagai form field
        fields = ['username', 'password1', 'password2']  

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile', None)
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        if profile:
            self.fields['role'].initial = profile.role
            self.fields['budget'].initial = profile.budget
            self.fields['profile_image'].initial = profile.profile_image

    def save(self, commit=True):
        user = super().save(commit=True)
        if commit:
            # user.save()
            # Buat Profile setelah user disave
            Profile.objects.create(
                user=user,
                role=self.cleaned_data['role'],  # Ambil dari cleaned_data
                budget=self.cleaned_data.get('budget', 0),
                profile_image=self.cleaned_data.get('profile_image', '')
            )
        return user

   

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
