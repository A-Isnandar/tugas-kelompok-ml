import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(BASE_DIR, 'excel', 'Perhitungan_Manual_Final.xlsx')
DATA_PATH = os.path.join(BASE_DIR, 'dataset', 'Mall_Customers.csv')

print("--- MEMULAI VALIDASI EXCEL VS PYTHON ---")


if not os.path.exists(DATA_PATH):
    print(f"[ERROR] Dataset tidak ditemukan di {DATA_PATH}")
    exit()

df = pd.read_csv(DATA_PATH)
X = df.iloc[:, [3, 4]].values
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42, n_init=10) 
y_kmeans = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_


if not os.path.exists(EXCEL_PATH):
    print(f"[ERROR] File Excel tidak ditemukan di {EXCEL_PATH}")
    print("Pastikan lu udah Save As file lu jadi .xlsx di folder excel/")
    exit()

print("[INFO] Membaca file Excel...")
try:
    df_excel = pd.read_excel(EXCEL_PATH)
except Exception as e:
    print(f"[ERROR] Gagal baca Excel: {e}")
    exit()


errors = 0
print("\n[Mengecek 200 Baris Data...]")

for i in range(len(df)):
    
    income, score = X[i]
    true_cluster = y_kmeans[i] + 1 
    
    
    true_distances = []
    for c in centroids:
        dist = np.sqrt((income - c[0])**2 + (score - c[1])**2)
        true_distances.append(dist)
    
   
    
    
    try:
        
        if 'Klaster' in df_excel.columns:
            col_klaster = 'Klaster'
        elif 'Cluster' in df_excel.columns:
            col_klaster = 'Cluster'
        else:
            raise KeyError("Kolom 'Klaster' tidak ditemukan!")

        excel_cluster_str = str(df_excel.iloc[i][col_klaster])
        
        
        if 'C' in excel_cluster_str:
            excel_cluster = int(excel_cluster_str.replace('C', ''))
        else:
            excel_cluster = int(float(excel_cluster_str))
            
        
        if excel_cluster != true_cluster:
            print(f"❌ BARIS {i+1} SALAH KLASTER! Excel: {excel_cluster}, Python: {true_cluster}")
            errors += 1
            continue

        
        
        col_jarak_c1 = None
        candidates = ['Jarak C1', 'Jarak_C1', 'JarakC1'] 
        
        for cand in candidates:
            if cand in df_excel.columns:
                col_jarak_c1 = cand
                break
        
        if col_jarak_c1 is None:
             raise KeyError("Kolom 'Jarak C1' (atau variasinya) tidak ditemukan!")

        
        val_jarak = df_excel.iloc[i][col_jarak_c1]
        
        
        if isinstance(val_jarak, str):
            val_jarak = float(val_jarak.replace(',', '.'))
        else:
            val_jarak = float(val_jarak)

        if abs(val_jarak - true_distances[0]) > 0.1: 
            print(f"⚠️ BARIS {i+1} JARAK BEDA. Excel: {val_jarak}, Python: {true_distances[0]:.2f}")
            errors += 1
            
    except KeyError as e:
        print(f"[ERROR] Masalah Kolom: {e}")
        print(f"Nama kolom yang ada di Excel lu: {list(df_excel.columns)}")
        exit()
    except Exception as e:
        print(f"[ERROR] Baris {i+1}: {e}")
        errors += 1



if errors == 0:
    print("\n✅ SEMPURNA! Data Excel 100% Sinkron dengan Python.")
else:
    print(f"\n❌ Ditemukan {errors} perbedaan. Cek baris-baris di atas.")