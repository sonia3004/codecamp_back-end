from django.contrib import admin
from django.urls import path, include  # 🔥 Ajoute "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('denonciations.urls')),  # 🔥 Gère les routes API
]
