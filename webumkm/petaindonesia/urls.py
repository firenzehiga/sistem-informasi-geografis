from django.urls import path
from . import views, view_peta

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('petasatu/', view_peta.petasatu, name='petasatu'),
    path('petadua/', view_peta.petadua, name='petadua'),
]
