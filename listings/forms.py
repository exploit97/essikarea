from django import forms
from django.contrib.auth.models import User
from .models import Propriete



class AddProperty(forms.ModelForm):
    class Meta:
        model = Propriete
        exclude = ['realtor','is_published']
        widgets = {
            
            'title': forms.TextInput(attrs={'class':'form-control '}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'ville':forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.TextInput(attrs={'class':'form-control'}),
            'arrondissement': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'bedroom': forms.NumberInput(attrs={'class':'form-control'}),
            'bathroom': forms.NumberInput(attrs={'class':'form-control'}),
            'garage': forms.NumberInput(attrs={'class':'form-control'}),
            'list_date': forms.DateInput(attrs={'class':'form-control'}),
            'sqft': forms.NumberInput(attrs={'class':'form-control'}),
            'lot_size': forms.NumberInput(attrs={'class':'form-control'}),
            'photo_main': forms.FileInput(attrs={'class':'form-control'}),
            'photo_1': forms.FileInput(attrs={'class':'form-control'}),
            'photo_2': forms.FileInput(attrs={'class':'form-control'}),
            'photo_3': forms.FileInput(attrs={'class':'form-control'}),
            'photo_4': forms.FileInput(attrs={'class':'form-control'}),
            'photo_5': forms.FileInput(attrs={'class':'form-control'}),
            'photo_6': forms.FileInput(attrs={'class':'form-control'}),
            
        }
            
    

   
    
   
               
