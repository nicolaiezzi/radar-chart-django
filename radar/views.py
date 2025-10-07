from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import SauvegardeRadar

def liste_profils(request):
    profils = SauvegardeRadar.objects.order_by('-date_sauvegarde')
    return render(request, "radar/liste.html", {"profils": profils})

def creer_profil(request):
    nom = f"Profil_{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    SauvegardeRadar.objects.create(
        nom=nom,
        parametres={f"param_{i}": 5 for i in range(1, 11)}
    )
    return redirect("liste_profils")

def radar_interactif(request, pk):
    profil = get_object_or_404(SauvegardeRadar, pk=pk)
    return render(request, "radar/radar_interactif.html", {"profil": profil})

def maj_parametre(request, pk):
    profil = get_object_or_404(SauvegardeRadar, pk=pk)
    param = request.POST.get("param")
    valeur = int(request.POST.get("valeur"))
    profil.parametres[param] = valeur
    profil.save()
    return JsonResponse({"success": True})

def supprimer_profil(request, pk):
    profil = get_object_or_404(SauvegardeRadar, pk=pk)
    if request.method == "POST":
        profil.delete()
        return redirect("liste_profils")
    return render(request, "radar/supprimer.html", {"profil": profil})
