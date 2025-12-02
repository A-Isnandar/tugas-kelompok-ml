# Tugas Kelompok Machine Learning

Proyek ini bertujuan untuk melakukan Segmentasi Pelanggan (Customer Segmentation) menggunakan algoritma K-Means Clustering. Kami menggunakan dataset pengunjung mall untuk mengelompokkan pelanggan berdasarkan perilaku belanja mereka (Pendapatan vs Skor Pengeluaran) guna membantu strategi pemasaran yang lebih tepat sasaran.


## STRUKTUR FOLDER

Berikut adalah struktur folder dari proyek ini:

Tugas_Kelompok_Mall/
├── dataset/
│ ├── Mall_Customers.csv (Dataset mentah sumber: Kaggle)
│ └── clustered_mall_customers.csv (Hasil data yang sudah diberi label klaster)
├── excel/
│ └── perhitungan_manual.xlsx (Bukti perhitungan manual Metode 1)
├── model/
│ └── kmeans_mall_model.pkl (Model K-Means yang sudah dilatih/disimpan)
├── result/
│ ├── tugas_kelompok_elbow.png (Grafik Elbow Method penentuan K optimal)
│ └── tugas_kelompok_cluster.png (Visualisasi hasil klasterisasi Scatter Plot)
├── src/
│ └── tugas_kelompok.py (Skrip Python utama untuk analisis & visualisasi)
└── README.md (Dokumentasi proyek ini)


## METODOLOGI PENGERJAAN

Tugas ini dikerjakan menggunakan dua metode pendekatan sesuai instruksi:

1. METODE MANUAL (Semi-Otomatis dengan Excel)

   - Dilakukan perhitungan manual algoritma K-Means pada sampel data (10 data pertama).
   - Mencakup perhitungan Jarak Euclidean, penentuan Klaster, dan pembaruan Centroid.
   - File pengerjaan dapat dilihat di folder: excel/perhitungan_manual.xlsx

2. METODE KOMPUTERISASI (Python)
   - Menggunakan bahasa pemrograman Python untuk memproses keseluruhan dataset (200 data).
   - Langkah-langkah:
     a. Feature Selection: Menggunakan fitur 'Annual Income' dan 'Spending Score'.
     b. Elbow Method: Menentukan jumlah klaster optimal (didapatkan K=5).
     c. Modelling: Melatih model K-Means dengan K=5.
     d. Visualisasi: Menghasilkan grafik persebaran klaster.
   - Skrip kode ada di: src/tugas_kelompok.py


## CARA MENJALANKAN PROGRAM

Untuk menjalankan analisis komputerisasi, ikuti langkah berikut:

1. Pastikan Python (3.11) sudah terinstal di komputer.

2. Install library yang dibutuhkan dengan menjalankan perintah di terminal:
   pip install pandas matplotlib seaborn scikit-learn joblib

3. Jalankan skrip utama dari terminal:
   python src/tugas_kelompok.py

4. Hasil visualisasi dan model akan otomatis muncul di folder 'result/' dan 'model/'.


## TEKNOLOGI YANG DIGUNAKAN

- Bahasa: Python 3.x
- Analisis Data: Pandas, NumPy
- Machine Learning: Scikit-Learn (K-Means)
- Visualisasi: Matplotlib, Seaborn
- Tools Lain: Microsoft Excel (untuk perhitungan manual)


## ANGGOTA KELOMPOK

1. MUHAMAD ARIO ISNANDAR (231011401602)  
2. ALI IBRAHIM (231011401607)  
3. HANA RIFDAH RIANRA (231011401383)  
4. OLIVIA RAMADHANI (231011402280)  
5. PUTRI AMALIA (231011401598)  
6. RIZKI ARTINIO PERMANA PUTRA (231011401590)
7. DORRA LADY AFISHE (231011402314)
