from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import SAFE_METHODS
from .models import Denonciation
from .serializers import DenonciationSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    🔥 Custom permission : 
    - Tout le monde peut LIRE les dénonciations
    - Seul l'auteur peut MODIFIER/SUPPRIMER ses propres dénonciations
    """

    def has_object_permission(self, request, view, obj):
        # 🔓 Autoriser tout le monde à lire
        if request.method in SAFE_METHODS:
            return True
        # 🔒 Autoriser seulement l'auteur à modifier/supprimer
        return obj.user == request.user or request.user.is_superuser

class DenonciationViewSet(viewsets.ModelViewSet):
    queryset = Denonciation.objects.all().order_by('-date_creation')  #  Trier par date (récentes en premier)
    serializer_class = DenonciationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 🔍 Définition des filtres disponibles
    filterset_fields = ['localisation', 'categorie', 'important']
    search_fields = ['titre', 'description']  # 🔎 Recherche textuelle
    ordering_fields = ['date_creation']  # ⏳ Trier par date de création

    def get_permissions(self):
        """ 🔥 Modifier les permissions selon l’action demandée """
        if self.action in ['list', 'retrieve']:  # 🔍 Tout le monde peut voir les dénonciations
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]  # 🔐 JWT requis pour poster/modifier/supprimer

    def perform_create(self, serializer):
        """ 🔥 Associer l'utilisateur connecté à la dénonciation """
        serializer.save(user=self.request.user)
