from rest_framework import serializers
from .models import Denonciation

class DenonciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denonciation
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}  # 🔥 Django ne demandera plus ce champ dans le POST

