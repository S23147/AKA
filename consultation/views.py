from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.contrib.auth.decorators import login_required
from .models import Consultation, Ordonnance, Prescription
from .forms import ConsultationForm, OrdonnanceForm
from patients.models import Patient

@login_required
def consultation_dashboard(request):
    """ Tableau de bord des consultations """
    return render(request, 'consultation/dashboard.html')

@login_required
def add_consultation(request, patient_id):
    """ Ajout d'une consultation pour un patient donné """
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = patient
            consultation.save()
            return redirect('creer_ordonnance', consultation_id=consultation.id)
    else:
        form = ConsultationForm()
    
    return render(request, 'consultation/add_consultation.html', {'form': form, 'patient': patient})

@login_required
def consultation_history(request, patient_id):
    """ Historique des consultations d'un patient """
    patient = get_object_or_404(Patient, id=patient_id)
    consultations = Consultation.objects.filter(patient=patient).order_by('-date')

    return render(request, 'consultation/consultation_history.html', {
        'patient': patient,
        'consultations': consultations
    })

@login_required
def creer_ordonnance(request, consultation_id):
    """ Ajout d'une ordonnance après consultation """
    consultation = get_object_or_404(Consultation, id=consultation_id)
    Medicament = apps.get_model('pharmacie', 'Medicament')
    medicaments = Medicament.objects.all()

    if request.method == "POST":
        form = OrdonnanceForm(request.POST)
        if form.is_valid():
            ordonnance = form.save(commit=False)
            ordonnance.consultation = consultation
            ordonnance.save()

            medicament_ids = request.POST.getlist('medicaments')
            if medicament_ids:
                for med_id in medicament_ids:
                    Prescription.objects.create(ordonnance=ordonnance, medicament_id=med_id, quantite=1)
            return redirect('consultation_history', patient_id=consultation.patient.pk)
    else:
        form = OrdonnanceForm()

    context = {
        'form': form,
        'consultation': consultation,
        'medicaments': medicaments,
    }
    return render(request, 'consultation/add_ordonnance.html', context)

@login_required
def edit_consultation(request, consultation_id):
    """ Modification d'une consultation """
    consultation = get_object_or_404(Consultation, id=consultation_id)
    
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation_history', patient_id=consultation.patient.pk)
    else:
        form = ConsultationForm(instance=consultation)
    
    return render(request, 'consultation/edit_consultation.html', {
        'form': form,
        'consultation': consultation,
    })
