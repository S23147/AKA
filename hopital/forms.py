from django import forms
from .models import Hopital, Laboratoire, Service

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hopital
        fields = ['nom_hopital', 'categorie', 'adresse_hopital', 'telephone']
        widgets = {
            'nom_hopital': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse_hopital': forms.Textarea(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LaboratoireForm(forms.ModelForm):
    class Meta:
        model = Laboratoire
        fields = ['nom', 'hopital', 'responsable']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'hopital': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
        }
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom', 'hopital', 'description', 'responsable']  # Ajout du responsable
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'hopital': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'})  # Sélection du responsable
        }
