# Generated by Django 5.1.6 on 2025-02-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denonciations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denonciation',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
