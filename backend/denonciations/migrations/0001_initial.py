# Generated by Django 5.1.6 on 2025-02-25 16:17

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Denonciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('categorie', models.CharField(choices=[('corruption', 'Corruption & Abus de pouvoir'), ('droits_humains', 'Violations des droits humains'), ('fraude', 'Fraudes & Crimes économiques'), ('sante_securite', 'Santé publique & Sécurité'), ('maltraitance_animale', 'Maltraitance animale')], max_length=50)),
                ('localisation', models.CharField(max_length=255)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
