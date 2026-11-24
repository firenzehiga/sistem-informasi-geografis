# Peta Tematik Pengangguran dan Faktor yang Mempengaruhinya di Pulau Jawa

Repositori ini (branch `qgis`) memuat berkas kerja, basis data geospasial, dan hasil analisis pemetaan tematik kartografi menggunakan **QGIS (Quantum GIS)** untuk mata kuliah **Sistem Informasi Geografis (SIG) - Semester 7**, Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF).

---

## 🎯 Lingkup Proyek (*Scope*)
- **Wilayah Cakupan**: Pulau Jawa, tingkat provinsi.
- **Unit Analisis**: 6 poligon batas administrasi provinsi:
  1. DKI Jakarta (`31`)
  2. Jawa Barat (`32`)
  3. Jawa Tengah (`33`)
  4. DI Yogyakarta (`34`)
  5. Jawa Timur (`35`)
  6. Banten (`36`)

---

## 💡 Latar Belakang & Rasional Pemilihan Topik (*Kenapa Topik Ini?*)

Pengangguran merupakan isu sosial-ekonomi nyata dan krusial yang berdampak langsung pada kesejahteraan masyarakat, pertumbuhan ekonomi, serta arah kebijakan pembangunan daerah. Pulau Jawa sebagai pusat gravitasi ekonomi nasional menyajikan dinamika spasial yang sangat kaya dan variatif:
- **DKI Jakarta & Jawa Barat**: Memiliki konsentrasi industri manufaktur besar dan perputaran modal tertinggi, namun tetap menghadapi Tingkat Pengangguran Terbuka (TPT) yang tinggi akibat derasnya arus migrasi tenaga kerja dan dinamika kualifikasi pasar kerja.
- **DI Yogyakarta**: Dikenal sebagai pusat pendidikan tinggi dengan proporsi lulusan perguruan tinggi tertinggi kedua (17.50%), memiliki TPT relatif rendah (3.46%), namun tingkat kemiskinannya tertinggi di Pulau Jawa (10.08%).
- **Jawa Tengah & Jawa Timur**: Menawarkan upah tenaga kerja yang kompetitif sehingga menjadi destinasi utama relokasi industri manufaktur padat karya.

Kelima indikator tematik yang dipilih saling berkaitan erat, memungkinkan dilakukannya analisis spasial mendalam untuk menjawab pertanyaan reflektif: *apakah provinsi dengan konsentrasi industri besar otomatis memiliki tingkat pengangguran yang rendah?* Seluruh indikator bersumber dari publikasi resmi BPS sehingga konsisten, dapat dipertanggungjawabkan, dan terus diperbarui secara berkala.

---

## 📊 Spesifikasi Struktur Data (`data_project01.csv`)

### 1. Kolom Wajib Identitas Wilayah (4 Kolom Wajib):
- `nama_wilayah`: Nama resmi provinsi di Pulau Jawa.
- `luas_wilayah_km2`: Luas daratan wilayah administrasi (km²).
- `populasi`: Jumlah penduduk per proyeksi kependudukan 2025 (jiwa).
- `tahun`: Tahun basis data analisis (`2025`).

### 2. Indikator Tematik Utama (5 Data Tematik Olahan):
- `tpt_persen`: Tingkat Pengangguran Terbuka (%).
- `persen_lulusan_pt`: Persentase penduduk berpendidikan tinggi (Diploma/Sarjana/Pascasarjana).
- `jumlah_industri_bs`: Jumlah industri manufaktur skala Besar dan Sedang (unit).
- `persen_miskin`: Persentase penduduk yang hidup di bawah garis kemiskinan (%).
- `ump_rupiah`: Besaran Upah Minimum Provinsi (Rupiah).

### Tabel Data Statistik Lengkap:
| Kode | Wilayah | Luas (km²) | Populasi (2025) | TPT (%) | Lulusan PT (%) | Industri Manufaktur (unit) | Penduduk Miskin (%) | UMP (Rp) |
|:---:|:---|---:|---:|---:|---:|---:|---:|---:|
| **31** | DKI Jakarta | 661.52 | 10,684,900 | 6.05% | 21.25% | 1,380 | 4.03% | Rp 5,396,760 |
| **32** | Jawa Barat | 35,377.76 | 50,345,200 | 6.77% | 10.89% | 8,224 | 6.78% | Rp 2,191,232 |
| **33** | Jawa Tengah | 32,800.69 | 37,892,300 | 4.66% | 7.58% | 5,078 | 9.39% | Rp 2,169,348 |
| **34** | DI Yogyakarta | 3,133.15 | 3,762,541 | 3.46% | 17.50% | 584 | 10.08% | Rp 2,264,080 |
| **35** | Jawa Timur | 47,803.49 | 41,810,000 | 3.88% | 9.48% | 6,553 | 9.35% | Rp 2,305,984 |
| **36** | Banten | 9,662.92 | 12,431,400 | 6.69% | 11.01% | 3,485 | 5.51% | Rp 2,905,119 |

---

## 🔍 Temuan Analisis Spasial (~150 Kata)

> Analisis peta tematik mengungkapkan fenomena menarik di Pulau Jawa: **keberadaan sentra industri manufaktur skala besar tidak serta-merta menjamin rendahnya Tingkat Pengangguran Terbuka (TPT).** Jawa Barat dan Banten yang menjadi episentrum industri nasional (memiliki 8.224 dan 3.485 unit industri besar/sedang) justru mencatat angka pengangguran tertinggi di Pulau Jawa, masing-masing sebesar 6,77% dan 6,69%. Hal ini mengindikasikan adanya daya tarik urbanisasi tenaga kerja dari berbagai daerah yang melampaui kapasitas serap industri formal lokal, serta adanya tantangan *skills gap*.
> 
> Di sisi lain, DI Yogyakarta mencatat TPT terendah (3,46%) dengan proporsi lulusan perguruan tinggi yang sangat tinggi (17,50%), meskipun jumlah industri besarnya paling sedikit (584 unit). Sektor jasa pendidikan, pariwisata, dan ekonomi kreatif terbukti efektif menyerap angkatan kerja terdidik, kendati persentase kemiskinannya masih bertengger di angka 10,08%. Sementara itu, Jawa Tengah dengan standar UMP terendah (Rp 2.169.348) mampu menjaga TPT pada level moderat (4,66%) berkat daya tarik investasi industri padat karya.

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
        ├── Layout - Tingkat Pengangguran Terbuka 2025 (_).png
        ├── Layout - Tingkat Penduduk Lulusan Perguruan Tinggi (_).png
        ├── Layout - Jumlah Industri Sedang dan Besar 2025 (unit).png
        ├── Layout - Persentase Penduduk Miskin (_).png
        └── Layout - Upah Minimum Provinsi.png
```

---

## 🗺️ Peta Tematik yang Dihasilkan

Peta disusun menggunakan kaidah kartografi resmi pada Print Layout QGIS (dilengkapi judul peta, arah mata angin, skala bar/angka, legenda klasifikasi interval bertingkat, sumber data resmi, dan grid koordinat):
1. **Peta Tingkat Pengangguran Terbuka (TPT) 2025**: Visualisasi sebaran persentase pengangguran di 6 provinsi Jawa.
2. **Peta Persentase Penduduk Lulusan Perguruan Tinggi**: Klasifikasi tingkat capaian pendidikan tinggi penduduk usia kerja.
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
- **Sumber Data Indikator Sosial-Ekonomi**: Badan Pusat Statistik Republik Indonesia ([bps.go.id](https://www.bps.go.id)):
  - *Tingkat Pengangguran Terbuka (TPT)*: Survei Angkatan Kerja Nasional (Sakernas) BPS.
  - *Luas Wilayah & Populasi*: BPS (Provinsi Dalam Angka & Proyeksi Kependudukan).
  - *Persentase Penduduk Miskin*: Survei Sosial Ekonomi Nasional (Susenas) BPS.
  - *Upah Minimum Provinsi (UMP)*: BPS & Kementerian Ketenagakerjaan RI (Kemnaker).
- **Data Spasial Batas Wilayah (GeoJSON)**: Menggunakan basis data batas wilayah administratif Indonesia yang disediakan oleh [Yusuf Syaifudin (@yusufsyaifudin/wilayah-indonesia)](https://github.com/yusufsyaifudin/wilayah-indonesia) serta repositori bahan perkuliahan SIG dosen.

---

## 👨‍💻 Pengembang
- **Nama**: Firenze Higa
- **Institusi**: Sekolah Tinggi Teknologi Terpadu Nurul Fikri (STT-NF)
- **Mata Kuliah**: Sistem Informasi Geografis (SIG) - Semester 7
