from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DenonciationViewSet

router = DefaultRouter()
router.register(r'denonciations', DenonciationViewSet, basename="denonciations")  # 🔥 Ajoute basename ici !

urlpatterns = [
    path('', include(router.urls)),
]
