from django.shortcuts import render
from django.http import HttpResponse

def petasatu(request):
    return render(request, 'petaindonesia/petasatu.html')

def petadua(request):
    return render(request, 'petaindonesia/petadua.html')

def petatiga(request):
    """
    Me-render template gabungan Pertemuan 11 (Slide 6, 8, & 9) di area Depok:
    Marker, Circle 500m, Polygon, GeoJSON Point (Kampus A STT-NF), & Provider Basemap.
    """
    return render(request, 'petaindonesia/petatiga.html')

def peta_provinsi(request):
    """
    Me-render template peta 34 provinsi Indonesia (Leaflet.js)
    yang me-load data spasial GPS dari static/json/provinces.json.
    """
    return render(request, 'petaindonesia/peta_provinsi.html')

def petani_jawa(request):
    """
    Me-render template peta tematik (choropleth) profil petani & lahan pertanian
    di 6 provinsi Pulau Jawa (GeoJSON multi-polygon + data non-spasial).
    """
    return render(request, 'petaindonesia/petani_jawa.html')



