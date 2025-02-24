from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DenonciationViewSet

# Création du routeur DRF
router = DefaultRouter()
router.register(r'denonciations', DenonciationViewSet)  # Déclare l'endpoint

urlpatterns = [
    path('', include(router.urls)),  # Inclut toutes les routes générées
]
