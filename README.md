# Project 1 QGIS — Pemetaan Tematik Sosial-Ekonomi & Ketenagakerjaan Pulau Jawa 2025

Repositori ini (branch `qgis`) memuat berkas kerja dan hasil analisis pemetaan geospasial desktop menggunakan **QGIS (Quantum GIS)** untuk mata kuliah **Sistem Informasi Geografis (SIG) - Semester 7**, Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF).

---

## 📌 Ringkasan Proyek

Proyek ini berfokus pada analisis geospasial tematik komparatif antar-provinsi di Pulau Jawa pada tahun 2025. Analisis mencakup relasi antara indikator ketenagakerjaan, tingkat pendidikan tinggi, persebaran sektor industri manufaktur, tingkat kemiskinan, serta upah minimum provinsi (UMP).

### Cakupan Wilayah (6 Provinsi):
1. **DKI Jakarta** (Kode: `31`)
2. **Jawa Barat** (Kode: `32`)
3. **Jawa Tengah** (Kode: `33`)
4. **DI Yogyakarta** (Kode: `34`)
5. **Jawa Timur** (Kode: `35`)
6. **Banten** (Kode: `36`)

---

## 📊 Indikator Data Statistik (`data_project01.csv`)

| Kode | Wilayah | Luas (km²) | Populasi (2025) | TPT (%) | Lulusan PT (%) | Industri Sedang/Besar (unit) | Penduduk Miskin (%) | UMP (Rp) |
|:---:|:---|---:|---:|---:|---:|---:|---:|---:|
| **31** | DKI Jakarta | 661.52 | 10,684,900 | 6.05% | 21.25% | 1,380 | 4.03% | Rp 5,396,760 |
| **32** | Jawa Barat | 35,377.76 | 50,345,200 | 6.77% | 10.89% | 8,224 | 6.78% | Rp 2,191,232 |
| **33** | Jawa Tengah | 32,800.69 | 37,892,300 | 4.66% | 7.58% | 5,078 | 9.39% | Rp 2,169,348 |
| **34** | DI Yogyakarta | 3,133.15 | 3,762,541 | 3.46% | 17.50% | 584 | 10.08% | Rp 2,264,080 |
| **35** | Jawa Timur | 47,803.49 | 41,810,000 | 3.88% | 9.48% | 6,553 | 9.35% | Rp 2,305,984 |
| **36** | Banten | 9,662.92 | 12,431,400 | 6.69% | 11.01% | 3,485 | 5.51% | Rp 2,905,119 |

---

## 🗂️ Struktur Direktori Proyek

```text
Project_Kelompok/
├── .gitignore                          # Pengabaian berkas sementara/backup QGIS
├── README.md                           # Dokumentasi proyek QGIS
│
└── Project_1_QGIS_Kelompok/
    ├── project_qgis1.qgz               # Berkas utama QGIS Project (layer, simbologi, styling)
    ├── pulau_jawa.gpkg                 # Basis data spasial GeoPackage Pulau Jawa
    │
    ├── Data/
    │   └── data_project01.csv          # Data tabular statistik sosial-ekonomi 2025
    │
    ├── poligon/                        # Vektor poligon batas administrasi provinsi (GeoJSON)
    │   ├── 31.geojson                  # DKI Jakarta
    │   ├── 32.geojson                  # Jawa Barat
    │   ├── 33.geojson                  # Jawa Tengah
    │   ├── 34.geojson                  # DI Yogyakarta
    │   ├── 35.geojson                  # Jawa Timur
    │   └── 36.geojson                  # Banten
    │
    └── Layout/                         # Hasil ekspor peta kartografi siap cetak (PNG)
        ├── Layout - Jumlah Industri Sedang dan Besar 2025 (unit).png
        ├── Layout - Persentase Penduduk Miskin (_).png
        ├── Layout - Tingkat Penduduk Lulusan Perguruan Tinggi (_).png
        ├── Layout - Tingkat Pengangguran Terbuka 2025 (_).png
        └── Layout - Upah Minimum Provinsi.png
```

---

## 🗺️ Peta Tematik yang Dihasilkan

Peta disusun menggunakan kaidah kartografi resmi pada Print Layout QGIS (dilengkapi judul peta, arah mata angin, skala bar/angka, legenda klasifikasi interval, sumber data, dan sistem koordinat):

1. **Peta Tingkat Pengangguran Terbuka (TPT) 2025**: Visualisasi sebaran persentase pengangguran di 6 provinsi Jawa.
2. **Peta Persentase Penduduk Lulusan Perguruan Tinggi**: Klasifikasi tingkat capaian pendidikan tinggi penduduk.
3. **Peta Sebaran Industri Sedang dan Besar**: Pemetaan konsentrasi fasilitas industri manufaktur skala menengah ke atas.
4. **Peta Persentase Penduduk Miskin**: Distribusi spasial tingkat kemiskinan per provinsi.
5. **Peta Upah Minimum Provinsi (UMP)**: Visualisasi perbandingan standar pengupahan regional tenaga kerja.

---

## 🛠️ Cara Membuka Proyek

1. Pastikan telah menginstal [QGIS](https://qgis.org/) versi 3.x (disarankan QGIS LTR).
2. Kloning repositori dengan branch `qgis`:
   ```bash
   git clone -b qgis https://github.com/firenzehiga/sistem-informasi-geografis.git
   ```
3. Buka aplikasi QGIS Desktop, lalu buka berkas proyek:
   - Jalur: `Project_1_QGIS_Kelompok/project_qgis1.qgz`
4. Seluruh layer vektor (`pulau_jawa.gpkg`, GeoJSON poligon) dan layout kartografi di Print Layout Manager akan otomatis terhubung.

---

## 🙏 Kredit & Sumber Data
- **Data Spasial Batas Wilayah (GeoJSON)**: Menggunakan data batas wilayah administratif Indonesia yang disediakan oleh [Yusuf Syaifudin (@yusufsyaifudin/wilayah-indonesia)](https://github.com/yusufsyaifudin/wilayah-indonesia).
- **Data Statistik Sosial-Ekonomi**: Badan Pusat Statistik (BPS) Republik Indonesia tahun 2025.

---

## 👨‍💻 Pengembang
- **Nama**: Firenze Higa
- **Institusi**: Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF)
- **Mata Kuliah**: Sistem Informasi Geografis (SIG) - Semester 7
