from django.shortcuts import render, redirect
from django.http import JsonResponse
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.Exceptions import NoCardException
from .models import SmartCard
from patients.models import Patient
from hopital.models import Hopital  # Assurez-vous que nous avons le modèle Hopital pour l'attribution via NFC
from .forms import PatientForm  # Assurez-vous d'avoir un formulaire pour le patient
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def add_patient(request):
    """Vue pour ajouter un patient à partir de la carte NFC"""
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            # Génération d'un identifiant unique pour l'utilisateur du patient
            if not patient.user:
                patient.user = User.objects.create_user(username=f"{patient.first_name}{patient.last_name}_{random.randint(1000, 9999)}", password="default_password")
            # Assigner l'hôpital via NFC ou logique spécifique
            if not patient.hopital:
                hopital = Hopital.objects.order_by('?').first()  # Assigner un hôpital aléatoire si non assigné
                patient.hopital = hopital
            patient.save()
            return redirect('patients:patient_list')  # Redirection vers la liste des patients après l'ajout
    else:
        form = PatientForm()
    
    return render(request, 'patients/add_patient.html', {'form': form})

def read_nfc_card(request):
    """Lecture d'une carte NFC et récupération du patient associé"""
    try:
        # Vérification de la présence de lecteurs NFC disponibles
        available_readers = readers()
        if not available_readers:
            return JsonResponse({"status": "error", "message": "Aucun lecteur NFC détecté."})

        reader = available_readers[0].createConnection()
        reader.connect()

        # Commande pour obtenir l'UID de la carte NFC
        GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        data, sw1, sw2 = reader.transmit(GET_UID)

        # Vérification si la lecture a réussi
        if sw1 == 0x90 and sw2 == 0x00:
            uid = toHexString(data)

            try:
                # Recherche de la carte dans la base de données
                card = SmartCard.objects.get(numero_carte=uid)
                patient = card.patient

                # Attribution automatique de l'hôpital via NFC
                # Ici, vous pouvez mettre en place une logique pour assigner un hôpital si nécessaire.
                # Par exemple, assigner aléatoirement un hôpital si ce n'est pas déjà fait
                if not patient.hopital:
                    hopital = Hopital.objects.order_by('?').first()  # Assigner un hôpital aléatoire
                    patient.hopital = hopital
                    patient.save()
                    message = f"Hôpital {hopital.nom_hopital} assigné à ce patient."
                else:
                    message = f"Le patient est déjà assigné à l'hôpital {patient.hopital.nom_hopital}."

                return JsonResponse({
                    "status": "success",
                    "uid": uid,
                    "message": message,
                    "patient": {
                        "id": patient.id,
                        "nom": patient.last_name,
                        "prenom": patient.first_name,
                        "date_naissance": patient.date_of_birth.strftime("%d-%m-%Y"),
                        "telephone": patient.phone_number,
                        "email": patient.email if patient.email else "Non spécifié",
                        "hopital": patient.hopital.nom if patient.hopital else "Non Assigné"
                    }
                })

            except SmartCard.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Aucun patient associé à cette carte NFC."})

        return JsonResponse({"status": "error", "message": f"Erreur de lecture NFC : {sw1:02X} {sw2:02X}"})

    except NoCardException:
        return JsonResponse({"status": "error", "message": "Aucune carte NFC détectée. Veuillez placer la carte sur le lecteur."})
    except Exception as e:
        return JsonResponse({"status": "error", "message": f"Erreur système : {str(e)}"})

def generate_smartcard(request, patient_id):
    """ Vue pour générer une carte intelligente pour un patient """
    patient = get_object_or_404(Patient, id=patient_id)
    
    # Vérification si le patient a déjà une carte intelligente
    if SmartCard.objects.filter(patient=patient).exists():
        return JsonResponse({"status": "error", "message": "Ce patient possède déjà une carte intelligente."})

    # Génération d'un numéro unique pour la carte
    card_number = f"SC-{random.randint(100000, 999999)}"
    
    # Création de la carte intelligente
    smartcard = SmartCard.objects.create(
        patient=patient,
        numero_carte=card_number
    )

    return JsonResponse({
        "status": "success",
        "message": f"Carte intelligente générée avec succès pour le patient {patient.first_name} {patient.last_name}.",
        "card_number": card_number
    })
