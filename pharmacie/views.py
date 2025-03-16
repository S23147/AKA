from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Medicament
from .forms import MedicamentForm

@login_required
def pharmacie_dashboard(request):
    return render(request, "pharmacie/dashboard.html")
@login_required
def add_medicament(request):
    """ Vue pour ajouter un médicament """
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicament_list')
    else:
        form = MedicamentForm()
    return render(request, 'pharmacie/add_medicament.html', {'form': form})

@login_required
def medicament_list(request):
    """ Vue pour afficher la liste des médicaments """
    medicaments = Medicament.objects.all()
    return render(request, 'pharmacie/medicament_list.html', {'medicaments': medicaments})

@login_required
def order_list(request):
    """ Vue pour afficher la liste des commandes en pharmacie """
    return render(request, 'pharmacie/orders.html')  # Assure-toi que ce fichier existe
