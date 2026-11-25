from django.urls import path
from . import views, view_peta

urlpatterns = [
    path('', views.landing, name='landing'),
    path('welcome/', views.welcome, name='welcome'),
    path('petasatu/', view_peta.petasatu, name='petasatu'),
    path('petadua/', view_peta.petadua, name='petadua'),
    path('petatiga/', view_peta.petatiga, name='petatiga'),
    path('petaindonesia/provinsi/', view_peta.peta_provinsi, name='peta_provinsi'),
    path('provinsi/', view_peta.peta_provinsi, name='provinsi_shortcut'),
    path('petaindonesia/petani_jawa/', view_peta.petani_jawa, name='petani_jawa'),
    path('petani_jawa/', view_peta.petani_jawa, name='petani_jawa_shortcut'),
]
