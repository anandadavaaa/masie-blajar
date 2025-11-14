# Program Pemilihan Pengurus Kelas

print("===== PEMILIHAN PENGURUS KELAS =====")
print()

# Daftar calon
calon_ketua = ["Kharis", "Ajie", "Bayu"]
calon_wakil = ["Reihan", "Ananda", "Muhammad"]
calon_bendahara = ["Maylani", "Casmita", "Ammay"]

# Menampilkan pilihan
print("Calon Ketua Kelas:")
for i, nama in enumerate(calon_ketua, start=1):
    print(f"{i}. {nama}")

pil_ketua = int(input("Pilih Ketua (1-3): "))
ketua_terpilih = calon_ketua[pil_ketua - 1]

print("\nCalon Wakil Ketua:")
for i, nama in enumerate(calon_wakil, start=1):
    print(f"{i}. {nama}")

pil_wakil = int(input("Pilih Wakil (1-3): "))
wakil_terpilih = calon_wakil[pil_wakil - 1]

print("\nCalon Bendahara:")
for i, nama in enumerate(calon_bendahara, start=1):
    print(f"{i}. {nama}")

pil_bendahara = int(input("Pilih Bendahara (1-3): "))
bendahara_terpilih = calon_bendahara[pil_bendahara - 1]

# Hasil akhir
print("\n===== HASIL PEMILIHAN =====")
print(f"Ketua Kelas     : {ketua_terpilih}")
print(f"Wakil Ketua     : {wakil_terpilih}")
print(f"Bendahara       : {bendahara_terpilih}")
print("============================")