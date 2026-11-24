# 🌐 WebGIS dengan Python Web Django Framework

Repositori ini memuat implementasi proyek **WebGIS (Web Geographic Information System)** berbasis framework **Django (MVT Architecture)** dan pustaka pemetaan client-side **Leaflet.js** untuk mata kuliah **Sistem Informasi Geografis (SIG) - Semester 7**, STT Terpadu Nurul Fikri.

Proyek ini mencakup materi praktikum **Pertemuan 10 (Dasar WebGIS & Integrasi API Gempa BMKG)** dan **Pertemuan 11 (Visualisasi Data Spasial GeoJSON & Peta Tematik Choropleth)**.

---

## 🚀 Fitur dan Modul Aplikasi

Proyek ini dibangun secara modular menggunakan 1 Django Project (`webumkm`) dan 2 Django Apps (`petaindonesia` dan `gempabumi`):

| Endpoint URL | Modul / App | Materi Perkuliahan | Deskripsi Fitur & Fungsionalitas |
|:---|:---|:---|:---|
| `/welcome/` | `petaindonesia` | Pertemuan 10 (Slide 9) | Endpoint verifikasi awal arsitektur MVT (*Model-View-Template*) dan perutean URL Django. |
| `/petasatu/` | `petaindonesia` | Pertemuan 10 (Slide 10) | **Peta Dasar Indonesia**: Integrasi Leaflet.js v1.9.4, batas wilayah nusantara (*bounds*), kontrol pengalih layer (*OpenStreetMap* & *Esri Satellite*), marker DKI Jakarta, skala metrik, serta pendeteksi koordinat interaktif saat peta diklik. |
| `/petadua/` | `petaindonesia` | Pertemuan 10 (Slide 11) | **Praktikum Mandiri 1 (Peta Jabodetabek)**: Pemetaan 5 kota metropolitan (Jakarta, Bogor, Depok, Tangerang, Bekasi) dengan *marker* berlabel permanen (*tooltip*), *featureGroup fitBounds*, dan **panel kontrol UI "Pilih kota"** dengan animasi kamera (*smooth flyTo*). |
| `/gempabumi/` | `gempabumi` | Pertemuan 10 (Slide 12) | **Praktikum Mandiri 2 (Monitoring Gempa Real-time BMKG)**: Menarik data 15 gempa terkini M 5.0+ dari API resmi BMKG secara *live* (dengan proteksi *offline fallback* otomatis), visualisasi *CircleMarker* berbasis kedalaman (Merah < 70 km, Kuning 70–300 km, Hijau > 300 km), ukuran radius proporsional magnitudo, legenda kartografi, serta bilah sisi (*sidebar*) interaktif dua arah. |
| `/petaindonesia/provinsi/` | `petaindonesia` | Pertemuan 11 (Slide 11) | **Praktikum Terpandu (Peta 34 Provinsi Indonesia)**: Pemuatan data spasial koordinat `provinces.json` dari direktori statis Django secara asinkron (`fetch`), sebaran 34 marker provinsi di nusantara, lencana kode wilayah ID, serta **kolom pencarian teks real-time** pada sidebar. *(Shortcut: `/provinsi/`)* |
| `/petaindonesia/petani_jawa/` | `petaindonesia` | Pertemuan 11 (Slide 12-13) | **Praktikum Mandiri (Peta Tematik Choropleth Petani Jawa)**: Integrasi 6 berkas poligon GeoJSON Jawa (`31.geojson` s/d `36.geojson`) dengan data statistik pertanian BPS 2024 (`petani_jawa.json`). Dilengkapi **filter 5 metrik pewarnaan dinamis** (Kepadatan Penduduk, Jumlah Petani, Luas Panen Padi, Populasi, Luas Wilayah), kartu info statistik interaktif (*hover/click*), serta legenda adaptif. *(Shortcut: `/petani_jawa/`)* |

---

## 🛠️ Struktur Direktori Proyek

```text
Project_WebGIS/
├── requirements.txt            # Dependensi pustaka Python
├── .gitignore                  # Berkas pengabaian Git (venv, cache, db)
├── README.md                   # Dokumentasi proyek lengkap
├── peta-indonesia.html         # Berkas template referensi Slide 10
├── gempaterkini.json           # Berkas data referensi BMKG Slide 12
│
└── webumkm/                    # Django Project Root (Outer Container)
    ├── manage.py               # Skrip manajemen baris perintah Django
    │
    ├── webumkm/                # Ruang Konfigurasi Pusat (Settings & Root URLs)
    │   ├── settings.py         # Pengaturan global, STATICFILES_DIRS, & SECURE_REFERRER_POLICY
    │   ├── urls.py             # Root URL dispatcher & static files serving
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── static/                 # Direktori Aset Statis Publik (Pertemuan 11)
    │   └── json/
    │       ├── provinces.json  # Data koordinat GPS 34 provinsi se-Indonesia
    │       ├── petani_jawa.json # Data non-spasial statistik petani & lahan (BPS 2024)
    │       ├── 31.geojson      # Poligon batas wilayah DKI Jakarta
    │       ├── 32.geojson      # Poligon batas wilayah Jawa Barat
    │       ├── 33.geojson      # Poligon batas wilayah Jawa Tengah
    │       ├── 34.geojson      # Poligon batas wilayah DI Yogyakarta
    │       ├── 35.geojson      # Poligon batas wilayah Jawa Timur
    │       └── 36.geojson      # Poligon batas wilayah Banten
    │
    ├── petaindonesia/          # App 1: Pemetaan Wilayah, Provinsi & Tematik Jawa
    │   ├── templates/petaindonesia/
    │   │   ├── petasatu.html   # Template Peta Indonesia
    │   │   ├── petadua.html    # Template Peta Jabodetabek + Panel Pilih Kota
    │   │   ├── peta_provinsi.html # Template Peta 34 Provinsi + Sidebar Search
    │   │   └── petani_jawa.html   # Template Peta Tematik Choropleth Jawa
    │   ├── views.py
    │   ├── view_peta.py        # Controller modular render peta Leaflet
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
# Windows (PowerShell)
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
- **Peta Dasar Indonesia (Pertemuan 10)**: [http://localhost:8000/petasatu/](http://localhost:8000/petasatu/)
- **Peta Interaktif Jabodetabek (Pertemuan 10)**: [http://localhost:8000/petadua/](http://localhost:8000/petadua/)
- **Monitoring Gempa Real-time BMKG (Pertemuan 10)**: [http://localhost:8000/gempabumi/](http://localhost:8000/gempabumi/)
- **Peta 34 Provinsi Indonesia (Pertemuan 11)**: [http://localhost:8000/petaindonesia/provinsi/](http://localhost:8000/petaindonesia/provinsi/)
- **Peta Tematik Choropleth Petani Jawa (Pertemuan 11)**: [http://localhost:8000/petaindonesia/petani_jawa/](http://localhost:8000/petaindonesia/petani_jawa/)

---

## 👨‍💻 Pengembang
- **Nama**: Firenze Higa
- **Institusi**: Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF)
- **Mata Kuliah**: Sistem Informasi Geografis (SIG) - Semester 7
