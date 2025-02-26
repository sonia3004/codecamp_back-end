from django.contrib.gis.db import models  # 🔥 Importation GIS pour PostGIS
from django.contrib.auth.models import User

class Denonciation(models.Model):
    CATEGORIES = [
        ('corruption', 'Corruption & Abus de pouvoir'),
        ('droits_humains', 'Violations des droits humains'),
        ('fraude', 'Fraudes & Crimes économiques'),
        ('sante_securite', 'Santé publique & Sécurité'),
        ('maltraitance_animale', 'Maltraitance animale'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    localisation = models.CharField(max_length=255)
    point = models.PointField(srid=4326, null=True, blank=True)  # ✅ Ajout de `srid=4326`
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} - {self.user.username}"
