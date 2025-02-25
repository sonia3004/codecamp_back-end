from rest_framework import viewsets, permissions
from .models import Denonciation
from .serializers import DenonciationSerializer

class DenonciationViewSet(viewsets.ModelViewSet):
    queryset = Denonciation.objects.all()  # 🔥 Ajoute ceci pour éviter l'erreur
    serializer_class = DenonciationSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔒 JWT obligatoire

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Denonciation.objects.all()
        return Denonciation.objects.filter(user=user)  # 🔥 Ne voir que ses propres dénonciations

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 🔥 Associer automatiquement l'utilisateur connecté
