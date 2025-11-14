import random
import time

def deteksi_mata_air(kedalaman):
    # Probabilitas meningkat jika makin dalam
    peluang = min(0.1 + kedalaman * 0.05, 0.9)
    return random.random() < peluang

def deteksi_batu(kedalaman):
    # Batu banyak di kedalaman sedang
    if 2 <= kedalaman <= 6:
        peluang = 0.6
    else:
        peluang = 0.3
    return random.random() < peluang

def rekomendasi(mata_air, batu):
    if mata_air and not batu:
        return "Lokasi sangat baik untuk digali! Ada mata air dan minim batu."
    elif mata_air and batu:
        return "Ada mata air, tetapi ada batu. Penggalian mungkin sedikit sulit."
    elif not mata_air and batu:
        return "Tidak ada mata air dan banyak batu. Tidak direkomendasikan."
    else:
        return "Tidak ada mata air, tetapi tanah aman. Boleh digali, namun kecil kemungkinan air."

print("=== AquaCheck — Simulasi Pengecekan Mata Air & Batu ===")

lokasi = input("Masukkan nama lokasi pengecekan: ")

kedalaman = random.randint(1, 10)  # deteksi otomatis seperti sonar simulasi
print("\nMengukur struktur tanah...")
time.sleep(1.5)

print(f"Kedalaman pengukuran: {kedalaman} meter")

# Cek kondisi tanah
mata_air = deteksi_mata_air(kedalaman)
batu = deteksi_batu(kedalaman)

print("\nHasil Deteksi:")
print(f"- Mata air terdeteksi: {'Ya' if mata_air else 'Tidak'}")
print(f"- Batu besar terdeteksi: {'Ada' if batu else 'Tidak ada'}")

# Rekomendasi
print("\nRekomendasi:")
print(rekomendasi(mata_air, batu))