# 🌐 WebGIS dengan Python Web Django Framework

Repositori ini memuat implementasi proyek **WebGIS (Web Geographic Information System)** berbasis framework **Django (MVT Architecture)** dan pustaka pemetaan client-side **Leaflet.js** untuk mata kuliah **Sistem Informasi Geografis (SIG) - Semester 7**, STT Terpadu Nurul Fikri.

---

## 🚀 Fitur dan Modul Aplikasi

Proyek ini dibangun secara modular menggunakan 1 Django Project (`webumkm`) dan 2 Django Apps (`petaindonesia` dan `gempabumi`):

| Endpoint URL | Modul / App | Deskripsi Fitur & Fungsionalitas |
|:---|:---|:---|
| `/welcome/` | `petaindonesia` | Endpoint verifikasi awal arsitektur MVT (*Model-View-Template*) dan perutean URL. |
| `/petasatu/` | `petaindonesia` | **Peta Dasar Indonesia**: Integrasi Leaflet.js v1.9.4, batas koordinat wilayah nusantara (*bounds*), kontrol pengalih layer (*OpenStreetMap* & *Esri Satellite*), marker DKI Jakarta, skala metrik, serta pendeteksi koordinat interaktif saat peta diklik. |
| `/petadua/` | `petaindonesia` | **Praktikum Mandiri 1 (Peta Jabodetabek)**: Pemetaan 5 kota metropolitan (Jakarta, Bogor, Depok, Tangerang, Bekasi) dengan *marker* berlabel permanen (*tooltip*), *featureGroup fitBounds*, dan **panel kustom kontrol UI "Pilih kota"** dengan animasi kamera halus (*smooth flyTo*). |
| `/gempabumi/` | `gempabumi` | **Praktikum Mandiri 2 (Monitoring Gempa Real-time BMKG)**: Menarik data terbuka 15 gempa terkini M 5.0+ dari API resmi BMKG secara *live* (dengan proteksi *offline fallback* otomatis), visualisasi *CircleMarker* berbasis kedalaman (Merah < 70 km, Kuning 70–300 km, Hijau > 300 km), ukuran radius proporsional magnitudo, legenda kartografi, serta bilah sisi (*sidebar*) interaktif dua arah. |

---

## 🛠️ Struktur Direktori Proyek

```text
Project_WebGIS/
├── requirements.txt            # Dependensi pustaka Python
├── .gitignore                  # Berkas pengabaian Git (venv, cache, db)
├── README.md                   # Dokumentasi proyek
├── peta-indonesia.html         # Berkas template referensi Slide 10
├── gempaterkini.json           # Berkas data referensi BMKG Slide 12
│
└── webumkm/                    # Django Project Root (Outer Container)
    ├── manage.py               # Skrip manajemen baris perintah Django
    │
    ├── webumkm/                # Ruang Konfigurasi Pusat (Settings & Root URLs)
    │   ├── settings.py         # Pengaturan global & SECURE_REFERRER_POLICY
    │   ├── urls.py             # Root URL dispatcher
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── petaindonesia/          # App 1: Pemetaan Dasar & Jabodetabek
    │   ├── templates/petaindonesia/
    │   │   ├── petasatu.html   # Template Peta Indonesia
    │   │   └── petadua.html    # Template Peta Jabodetabek + Panel Pilih Kota
    │   ├── views.py
    │   ├── view_peta.py        # Controller khusus render peta
    │   └── urls.py
    │
    └── gempabumi/              # App 2: Pemantauan Gempa Real-time BMKG
        ├── data/
        │   └── gempaterkini.json # Berkas cadangan lokal (Offline Fallback)
        ├── templates/gempabumi/
        │   └── gempaterkini.html # Template Peta Gempa + Sidebar
        ├── views.py            # Controller konsumsi API BMKG & klasifikasi spasial
        └── urls.py
```

---

## ⚙️ Panduan Instalasi & Menjalankan Proyek

### 1. Kloning Repositori & Pindah ke Branch `webgis`
```bash
git clone https://github.com/firenzehiga/sistem-informasi-geografis.git
cd sistem-informasi-geografis
git checkout webgis
```

### 2. Buat dan Aktifkan Virtual Environment
```bash
# Windows
python -m venv webgis
.\webgis\Scripts\activate

# Linux / macOS
python3 -m venv webgis
source webgis/bin/activate
```

### 3. Pasang Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Development Server
```bash
cd webumkm
python manage.py runserver
```

Akses aplikasi pada peramban melalui URL:
- Peta Dasar Indonesia: `http://localhost:8000/petasatu/`
- Peta Interaktif Jabodetabek: `http://localhost:8000/petadua/`
- Monitoring Gempa BMKG: `http://localhost:8000/gempabumi/`

---

## 👨‍💻 Pengembang
- **Nama**: Firenze Higa
- **Institusi**: Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF)
- **Mata Kuliah**: Sistem Informasi Geografis (SIG)
