from django.shortcuts import render, redirect
from .models import Hopital
from .forms import hopitalForm

def add_hopital(request):
    """ Vue pour ajouter un hôpital """
    if request.method == 'POST':
        form = hopitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hopital_list')  
    else:
        form = hopitalForm()
    return render(request, 'hopital/add_hopital.html', {'form': form})

def hopital_list(request):
    """ Vue pour afficher la liste des hôpitaux """
    hopitaux = Hopital.objects.all()
    return render(request, 'hopital/hopital_list.html', {'hopitaux': hopitaux})
