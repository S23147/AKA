from django import forms
from .models import Consultation, Ordonnance  # Ajoutez l'importation du modèle Ordonnance
from pharmacie.models import Medicament

class ConsultationForm(forms.ModelForm):
    """ Formulaire pour ajouter/modifier une consultation """
    class Meta:
        model = Consultation
        fields = [
            'motif_consultation', 'type_consultation', 'notes_consultation',
            'poids', 'taille', 'pression_arterielle', 'temperature',
            'frequence_cardiaque', 'symptomes', 'diagnostic', 'traitement_recommande'
        ]
        widgets = {
            'motif_consultation': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'type_consultation': forms.TextInput(attrs={'class': 'form-control'}),
            'notes_consultation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'symptomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostic': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'traitement_recommande': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'poids': forms.NumberInput(attrs={'class': 'form-control'}),
            'taille': forms.NumberInput(attrs={'class': 'form-control'}),
            'pression_arterielle': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'frequence_cardiaque': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OrdonnanceForm(forms.ModelForm):
    medicaments = forms.ModelMultipleChoiceField(
        queryset=Medicament.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Correction ici pour éviter une erreur si aucun médicament n'est sélectionné
        label="Sélectionnez les médicaments"
    )

    class Meta:
        model = Ordonnance  # Assurez-vous que Ordonnance est bien défini et importé
        fields = ['medicaments', 'instructions']
        widgets = {
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
