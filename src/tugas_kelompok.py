import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import joblib



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
RESULT_DIR = os.path.join(BASE_DIR, "result")
MODEL_DIR = os.path.join(BASE_DIR, "model")


os.makedirs(RESULT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

print("--- Memulai Tugas Kelompok: Segmentasi Pelanggan Mall (K-Means) ---")



file_path = os.path.join(DATASET_DIR, "Mall_Customers.csv")

try:
    df = pd.read_csv(file_path)
    print(f"\n[INFO] Data berhasil dimuat! Ukuran: {df.shape}")
    print(df.head())
except FileNotFoundError:
    print(f"\n[ERROR] File tidak ditemukan di: {file_path}")
    print("Tolong download dataset 'Mall Customer Segmentation' dan taruh di folder 'dataset/'")
    exit()




X = df.iloc[:, [3, 4]].values 

print(f"\n[INFO] Fitur yang digunakan: Annual Income & Spending Score")


print("\n[PROCESS] Menghitung Elbow Method untuk mencari jumlah klaster optimal...")

wcss = [] 
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


plt.figure(figsize=(10,6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('The Elbow Method (Mencari K Optimal)')
plt.xlabel('Jumlah Klaster (K)')
plt.ylabel('WCSS (Inersia)')
plt.grid(True)


elbow_path = os.path.join(RESULT_DIR, "tugas_kelompok_elbow.png")
plt.savefig(elbow_path)
print(f"[OUTPUT] Grafik Elbow Method disimpan di: {elbow_path}")
plt.close() 



k_optimal = 5
print(f"\n[PROCESS] Melakukan Klasterisasi dengan K={k_optimal}...")

kmeans = KMeans(n_clusters=k_optimal, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)


df['Cluster'] = y_kmeans



df.to_csv(os.path.join(DATASET_DIR, "clustered_mall_customers.csv"), index=False)


print("[PROCESS] Membuat Visualisasi Hasil Klaster...")

plt.figure(figsize=(12,8))



plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 50, c = 'red', label = 'Cluster 1 (Hemat?)')

plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Cluster 2 (Rata-rata)')

plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 50, c = 'green', label = 'Cluster 3 (Target Utama)')

plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 50, c = 'cyan', label = 'Cluster 4 (Impulsif?)')

plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 50, c = 'magenta', label = 'Cluster 5 (Sultan?)')


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 200, c = 'yellow', label = 'Centroids', edgecolors='black', marker='*')

plt.title('Hasil Klasterisasi Pelanggan Mall')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)


cluster_path = os.path.join(RESULT_DIR, "tugas_kelompok_cluster.png")
plt.savefig(cluster_path)
print(f"[OUTPUT] Visualisasi Klaster disimpan di: {cluster_path}")
plt.close()


model_path = os.path.join(MODEL_DIR, "kmeans_mall_model.pkl")
joblib.dump(kmeans, model_path)
print(f"\n[OUTPUT] Model K-Means disimpan di: {model_path}")

print("\n--- Selesai! Silakan cek folder 'result' dan 'model' ---")