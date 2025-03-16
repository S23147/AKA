from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

@login_required
def custom_login(request):
    """ Vue personnalisée pour la connexion des utilisateurs """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_page = request.POST.get("next", "/")  # Rediriger vers la page d'accueil par défaut si "next" est vide
            
            # Redirection en fonction du rôle
            role_redirects = {
                'superadmin': 'superadmin_dashboard',
                'ministere': 'ministere_dashboard',
                'services': 'services_dashboard',
                'pharmacien': 'pharmaceutique_dashboard',
                'admin': 'admin_dashboard',
                'medecin': 'medecin_dashboard',
                'patient': 'patient_dashboard'
            }

            role_name = user.role.lower() if hasattr(user, 'role') else None
            redirect_to = role_redirects.get(role_name, '/')
            return redirect(redirect_to)
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('login')
    return render(request, 'patients/login.html')
