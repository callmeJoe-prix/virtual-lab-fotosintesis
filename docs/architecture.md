# Arsitektur Aplikasi Virtual Photosynthesis Lab

Aplikasi menggunakan pola modular:

## 1. app.py
- Antarmuka pengguna (UI)
- Input parameter
- Menjalankan simulasi
- Menampilkan grafik dan hasil

## 2. modules/simulator.py
Menghitung:
- Light response curve (non-rectangular hyperbola)
- Produksi oksigen berbasis suhu & CO₂

## 3. modules/graph.py
- Plot kurva respon cahaya
- Grafik produksi O₂

## 4. modules/utils.py
- Loader file JSON

## 5. data/
- Parameter fisiologi tanaman
