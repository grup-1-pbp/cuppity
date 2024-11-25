from django import forms
from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'gambar_url']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control'}),
            'gambar_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
