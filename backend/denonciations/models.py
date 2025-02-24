from django.db import models

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
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

