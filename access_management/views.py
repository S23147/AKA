from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed

@login_required
def services_dashboard(request):
    return render(request, 'access_management/services_dashboard.html')

@login_required
def redirect_user(request):
    """ Redirige l'utilisateur selon son rôle """
    user = request.user
    if user.role == 'superadmin':
        return redirect('superadmin_dashboard')
    elif user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'medecin':
        return redirect('medecin_dashboard')
    elif user.role == 'patient':
        return redirect('patient_dashboard')
    elif user.role == 'pharmacien':
        return redirect('pharmaceutique_dashboard')
    elif user.role == 'ministere':
        return redirect('ministere_dashboard')
    elif user.role == 'services':
        return redirect('services_dashboard')
    else:
        return redirect('/')  # Redirection par défaut si aucun rôle n'est trouvé

@login_required
def admin_dashboard(request):
    return render(request, 'access_management/admin_dashboard.html')

@login_required
def superadmin_dashboard(request):
    return render(request, 'access_management/superadmin_dashboard.html')

@login_required
def medecin_dashboard(request):
    return render(request, 'access_management/medecin_dashboard.html')

@login_required
def patient_dashboard(request):
    return render(request, 'access_management/patient_dashboard.html')

@login_required
def pharmacien_dashboard(request):
    return render(request, 'access_management/pharmacien_dashboard.html')

@login_required
def ministere_dashboard(request):
    return render(request, 'access_management/ministere_dashboard.html')

@login_required
def personnel_admin_dashboard(request):
    return render(request, 'access_management/personnel_admin_dashboard.html')

@login_required
def bureau_entree_dashboard(request):
    return render(request, 'access_management/bureau_entree_dashboard.html')
@csrf_exempt
def custom_logout(request):
    """ Gérer la déconnexion avec une requête POST uniquement """
    if request.method == "POST":
        logout(request)
        return redirect(reverse("login"))
    return HttpResponseNotAllowed(["POST"])
