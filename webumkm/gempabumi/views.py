from django.shortcuts import render
from pathlib import Path
import requests
import json

BMKG_GEMPA_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
LOCAL_FALLBACK_FILE = Path(__file__).resolve().parent / "data" / "gempaterkini.json"

def gempaterkini(request):
    """
    Mengambil 15 data gempa M 5.0+ terbaru dari API BMKG (dengan fallback ke data lokal
    jika koneksi internet terputus atau server BMKG tidak dapat diakses),
    mengategorikan kedalaman spasial, dan merendernya pada antarmuka peta Leaflet.
    """
    daftar_gempa = []
    waktu_update = ""
    error_msg = None
    mode_sumber = "Live API BMKG"

    try:
        # 1. Coba ambil data terbaru secara online
        response = requests.get(BMKG_GEMPA_URL, timeout=5)
        response.raise_for_status()
        data_json = response.json()
    except Exception as e:
        # 2. Jika gagal/offline, gunakan data fallback lokal
        mode_sumber = "Data Cadangan Lokal (Offline Fallback)"
        if LOCAL_FALLBACK_FILE.exists():
            try:
                with open(LOCAL_FALLBACK_FILE, "r", encoding="utf-8") as f:
                    data_json = json.load(f)
            except Exception as read_err:
                error_msg = f"Gagal membaca file fallback: {str(read_err)}"
                data_json = {}
        else:
            error_msg = f"Koneksi BMKG gagal dan file fallback tidak ditemukan: {str(e)}"
            data_json = {}

    raw_gempa = data_json.get('Infogempa', {}).get('gempa', [])
    
    for idx, item in enumerate(raw_gempa):
        # Parsing koordinat: format "lintang,bujur" (misal: "-6.03,131.62")
        coords_split = [x.strip() for x in item.get('Coordinates', '0,0').split(',')]
        lat = float(coords_split[0]) if len(coords_split) > 0 else 0.0
        lng = float(coords_split[1]) if len(coords_split) > 1 else 0.0

        # Parsing kedalaman integer (misal "115 km" -> 115)
        depth_str = item.get('Kedalaman', '0').replace(' km', '').strip()
        try:
            depth_km = int(depth_str)
        except ValueError:
            depth_km = 0

        # Parsing magnitudo float
        try:
            mag = float(item.get('Magnitude', '0'))
        except ValueError:
            mag = 0.0

        # Klasifikasi warna kedalaman (Sesuai panduan Slide 12 BMKG):
        # 1. Dangkal (< 70 km)     -> Merah (#ef4444)
        # 2. Menengah (70 - 300 km) -> Kuning/Oranye (#f59e0b)
        # 3. Dalam (> 300 km)       -> Hijau (#10b981)
        if depth_km < 70:
            kategori_kedalaman = "Dangkal"
            warna = "#ef4444"
        elif depth_km <= 300:
            kategori_kedalaman = "Menengah"
            warna = "#f59e0b"
        else:
            kategori_kedalaman = "Dalam"
            warna = "#10b981"

        # Radius lingkaran proporsional terhadap magnitudo
        radius = max(6, int(mag * 3.2))

        item_gempa = {
            'no': idx + 1,
            'tanggal': item.get('Tanggal', ''),
            'jam': item.get('Jam', ''),
            'datetime': item.get('DateTime', ''),
            'coordinates': item.get('Coordinates', ''),
            'lat': lat,
            'lng': lng,
            'lintang': item.get('Lintang', ''),
            'bujur': item.get('Bujur', ''),
            'magnitude': item.get('Magnitude', '0'),
            'magnitude_float': mag,
            'kedalaman': item.get('Kedalaman', ''),
            'depth_km': depth_km,
            'depth_category': kategori_kedalaman,
            'color': warna,
            'radius': radius,
            'wilayah': item.get('Wilayah', ''),
            'potensi': item.get('Potensi', 'Tidak berpotensi tsunami')
        }
        daftar_gempa.append(item_gempa)

    if daftar_gempa:
        waktu_update = f"{daftar_gempa[0]['tanggal']} - {daftar_gempa[0]['jam']}"

    context = {
        'daftar_gempa': daftar_gempa,
        'json_gempa': json.dumps(daftar_gempa),
        'total_gempa': len(daftar_gempa),
        'waktu_update': waktu_update,
        'mode_sumber': mode_sumber,
        'error_msg': error_msg,
    }

    return render(request, 'gempabumi/gempaterkini.html', context)
