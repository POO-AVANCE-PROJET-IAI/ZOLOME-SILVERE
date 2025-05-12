"""
URL configuration for santeplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zolome_utilisateurs.urls', namespace='zolome_utilisateurs')),
    path('', include('zolome_patients.urls', namespace='zolome_patients')),
    path('', include('zolome_medecins.urls', namespace='zolome_medecins')),
    path('', include('zolome_consultations.urls', namespace='zolome_consultations')),
    path('', include('zolome_ordonnances.urls', namespace='zolome_ordonnances')),
    path('', include('zolome_factures.urls', namespace='zolome_factures')),
    path('parametres/', include('zolome_parametres.urls', namespace='zolome_parametres')),
    path('', lambda request: redirect('zolome_utilisateurs:login'), name='root'),
]
