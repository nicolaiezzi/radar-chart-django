from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_profils, name='liste_profils'),
    path('creer/', views.creer_profil, name='creer_profil'),
    path('<int:pk>/radar/', views.radar_interactif, name='radar_interactif'),
    path('<int:pk>/maj/', views.maj_parametre, name='maj_parametre'),
    path('<int:pk>/supprimer/', views.supprimer_profil, name='supprimer_profil'),
]
