from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Patient
from hopital.models import Hopital
from pharmacie.models import Medicament
from .forms import PatientForm, PrescriptionForm
import random
from consultation.models import Consultation
from hopital.models import AnalyseMedicale
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from django.contrib.auth import views as auth_views  # Correction ici

User = get_user_model()

def custom_login(request):
    """ Vue personnalisée pour la connexion des utilisateurs """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Rediriger vers la page d'accueil par défaut si "next" est vide
            next_url = request.GET.get('next', 'home')  # Vérifier l'URL de redirection
            if user.role == 'superadmin':
                return redirect('superadmin_dashboard')
            elif user.role == 'ministere':
                return redirect('ministere_dashboard')
            elif user.role == 'services':
                return redirect('services_dashboard')
            elif user.role == 'pharmacien':
                return redirect('pharmaceutique_dashboard')
            elif user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'medecin':
                return redirect('medecin_dashboard')
            elif user.role == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect(next_url)  # Redirection vers next si spécifié
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('login')
    return render(request, 'patients/login.html')

@login_required
def superadmin_dashboard(request):
    """ Tableau de bord pour le super administrateur """
    if request.user.role != 'superadmin':
        messages.error(request, "Vous n'avez pas les droits nécessaires pour accéder à cette page.")
        return redirect('home')

    health_statistics = {
        'total_patients': Patient.objects.count(),
        'total_consultations': Consultation.objects.count(),
        'total_laboratory_tests': AnalyseMedicale.objects.count(),
    }

    stock_data = {
        'total_medicines': Medicament.objects.count(),
        'medicines_in_stock': Medicament.objects.filter(stock_quantity__gt=0).count(),
    }

    return render(request, 'superadmin/dashboard.html', {
        'health_statistics': health_statistics,
        'stock_data': stock_data
    })

@login_required
def ministere_dashboard(request):
    """ Tableau de bord pour le ministère de la santé """
    if request.user.role != 'ministere':
        messages.error(request, "Vous n'avez pas les droits nécessaires pour accéder à cette page.")
        return redirect('home')

    health_statistics = {
        'total_patients': Patient.objects.count(),
        'total_consultations': Consultation.objects.count(),
        'total_laboratory_tests': AnalyseMedicale.objects.count(),
    }

    return render(request, 'ministere/dashboard.html', {'health_statistics': health_statistics})

@login_required
def services_dashboard(request):
    """ Tableau de bord pour les services médicaux """
    if request.user.role != 'services':
        messages.error(request, "Vous n'avez pas les droits nécessaires pour accéder à cette page.")
        return redirect('home')

    return render(request, 'services/dashboard.html')

@login_required
def pharmacie_dashboard(request):
    """ Tableau de bord pour les pharmaciens """
    if request.user.role != 'pharmacien':
        messages.error(request, "Vous n'avez pas les droits nécessaires pour accéder à cette page.")
        return redirect('home')

    return render(request, 'pharmacie/dashboard.html')

@login_required
def dashboard(request):
    """ Tableau de bord générique pour l'utilisateur """
    if request.user.role not in ['admin', 'medecin', 'pharmacien']:
        messages.error(request, "Vous n'avez pas accès à ce tableau de bord.")
        return redirect('home')
    return render(request, 'patients/dashboard.html')

@login_required
def patient_list(request):
    """ Liste des patients """
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
def add_patient(request):
    """ Vue pour ajouter un patient """
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            if not patient.user:
                patient.user = User.objects.create_user(username=f"{patient.first_name}{patient.last_name}_{random.randint(1000, 9999)}", password="default_password")
            if not patient.hopital:
                hopital = Hopital.objects.order_by('?').first()
                patient.hopital = hopital
            patient.save()
            messages.success(request, "Le patient a été ajouté avec succès !")
            return redirect("patients:patient_list")
    else:
        form = PatientForm()

    return render(request, "patients/add_patient.html", {"form": form})

@login_required
def edit_patient(request, patient_id):
    """ Vue pour éditer les informations d'un patient """
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Les informations du patient ont été mises à jour avec succès !")
            return redirect('patients:patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})

@login_required
def get_patients(request):
    """ Retourne la liste des patients sous format JSON pour l'API """
    patients = Patient.objects.all().values("id", "last_name", "first_name", "date_of_birth", "phone_number", "email")
    return JsonResponse({"patients": list(patients)})

@login_required
def add_prescription(request, patient_id):
    """ Vue pour ajouter une prescription à un patient """
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = patient
            prescription.prescribed_by = request.user
            prescription.save()
            messages.success(request, "La prescription a été ajoutée avec succès !")
            return redirect("patients:patient_list")
    else:
        form = PrescriptionForm()

    return render(request, "patients/add_prescription.html", {"form": form, "patient": patient})
