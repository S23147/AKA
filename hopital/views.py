from django.shortcuts import render, redirect
from .models import Hopital, Laboratoire, Service
from .forms import HospitalForm, LaboratoireForm, ServiceForm
from django.contrib import messages

def add_hospital(request):
    """ Vue pour ajouter un hôpital """
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'hôpital a été ajouté avec succès.")
            return redirect('hopital:hopital_list')  # Redirection après ajout
    else:
        form = HospitalForm()
    return render(request, 'hopital/add_hopital.html', {'form': form})

def hopital_list(request):
    """ Vue pour afficher la liste des hôpitaux """
    hopitaux = Hopital.objects.all()
    return render(request, 'hopital/hopital_list.html', {'hopitaux': hopitaux})

def add_service(request):
    """ Vue pour ajouter un service à l'hôpital """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le service a été ajouté avec succès.")
            return redirect('hopital:hopital_list')
    else:
        form = ServiceForm()
    return render(request, 'hopital/add_service.html', {'form': form})

def add_laboratoire(request):
    """ Vue pour ajouter un laboratoire à l'hôpital """
    if request.method == 'POST':
        form = LaboratoireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le laboratoire a été ajouté avec succès.")
            return redirect('hopital:hopital_list')
    else:
        form = LaboratoireForm()
    return render(request, 'hopital/add_laboratoire.html', {'form': form})

def assign_patient_to_hopital(request, patient_id, hopital_id):
    """ Assigner un patient à un hôpital """
    patient = Patient.objects.get(id=patient_id)
    hopital = Hopital.objects.get(id=hopital_id)
    patient.hopital = hopital
    patient.save()
    messages.success(request, "Le patient a été assigné à l'hôpital avec succès.")
    return redirect('patients:patient_list')
