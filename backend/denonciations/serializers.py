from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Denonciation

class DenonciationSerializer(GeoFeatureModelSerializer):  # 🔥 Utilisation du serializer géospatial
    class Meta:
        model = Denonciation
        geo_field = "point"  # 🔥 Indiquer que "point" est un champ géospatial
        fields = ('id', 'titre', 'description', 'categorie', 'localisation', 'point', 'date_creation', 'user')
        extra_kwargs = {'user': {'read_only': True}}  # 🔥 Django ne demandera plus ce champ dans le POST
