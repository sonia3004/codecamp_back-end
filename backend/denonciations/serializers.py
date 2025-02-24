from rest_framework import serializers
from .models import Denonciation

class DenonciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denonciation
        fields = '__all__'
