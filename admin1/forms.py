
from django.forms import ModelForm
from django import forms
from django.db.models import fields
from django.forms import widgets
from bookapp.models  import *

class AddBookForm(ModelForm):
    
    # title = forms.CharField(max_length=100, widget =forms.TextInput(attrs={
    #     'class':'form-control', 'placeholder':'Masukan judul Buku'
    # }))
    
    # slug = forms.SlugField(max_length=100, widget = forms.TextInput(attrs={
    #     'class':'form-control', 'placeholder':'Masukan Slug Teks'
    # }))
    
    # cover_image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class':'form-control'
    # }))
    
    # author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    #     'class':'form-control', 'placeholder':'Masukan nama Pengarang'
    # }))
    
    # summary = forms.CharField(widget=forms.Textarea(attrs={
    #     'class':'form-control'
    # }))
    
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        
    # }))
    
    # pdf = forms.FileField(widget=forms.FileInput(attrs={
    #     'class':'form-control'
    # }))
    
    
   
    class Meta:
        model = Book
        exclude = ('slug','recommended_books', 'fiction_books', 'business_books')
        
        widgets = {
            'title': forms.TextInput({'class':'form-control', 'placeholder':'Masukan Judul Buku'}),
            'slug' : forms.TextInput({'class':'form-control', 'placeholder':'Masukan Slug Teks',}),
            'cover_image' : forms.FileInput({'class':'form-control'}),
            'author' : forms.TextInput({'class':'form-control', 'placeholder':'Masukan Nama Pengarang'}),
            'summary' : forms.Textarea({'class':'form-control'}),
            'category' : forms.CheckboxSelectMultiple({}),
            'pdf' : forms.FileInput({'class':'form-control'}),
            
        }

class BookSearchForm(ModelForm):
    
    class Meta:
        model = BookSearch
        fields = ['name_of_book']
    
        widgets = {
            'name_of_book':forms.TextInput({'class':'form-control', 'type':'search', 'placeholder':'Search', 'aria-label':'Search', 'data-width':'250'})
        }