from django import forms
from .models import Buku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = "__all__"  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama judul'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama Penulis'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'book_cover': forms.FileInput(attrs={'class': 'form-control', 'for': 'coverInput'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control', 'for': 'coverInput'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Masukkan deskripsi buku'}),
        }