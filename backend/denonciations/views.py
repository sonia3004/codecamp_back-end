from rest_framework import viewsets
from .models import Denonciation
from .serializers import DenonciationSerializer

class DenonciationViewSet(viewsets.ModelViewSet):
    queryset = Denonciation.objects.all().order_by('-date_creation')
    serializer_class = DenonciationSerializer

